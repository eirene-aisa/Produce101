'''
토끼단 화이팅

GOAL : 
최민기 직캠 영상 페이지에 접속 후
- 연속 재생 해제 / 전체 댓글을 누르고 / 팝업 플레이어 끄기
- 댓글에서 좋아요 버튼 상태 체크 후 클릭해주는 코드

TO USE :
python 3.5 / Selenium 을 사용하는 코드입니다.

코드의 binary 변수에 다운받은 크롬 웹드라이버 경로를 써주세요.
NICKNAME, 네이버 아이디, 비밀번호를 상황에 맞게 입력해주세요.

WARNING :
네이버 댓글 로딩에 맞추다 보니 빠르지는 않습니다.

실행이 되면 브라우저 뜬 후 바로 최대화 해주시고요, 
플레이어 정지 -> 연속 재생 해제 후 4초가량 이후
전체 댓글로 넘어가고 팝업된 비디오를 끈 뒤 좋아요를 누르기 시작합니다.
실행 중에 클릭을 하면 실행이 멈추고,
댓글을 누르는 사이사이 스크롤 정도만 허락됩니다ㅜㅠ
스크롤도 막 하시면 좋아요 누르는 댓글을 건너뛰어요!

인터넷 환경에 따라 time.sleep()을 이용해 일시정지하는 시간을 조정해야 합니다.
'''
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

url_login = "https://nid.naver.com/nidlogin.login"
url_hit = "http://tv.naver.com/v/1747159/list/132312"

NICKNAME = "도파" # 본인 별명으로 수정

def main():
  binry = "C:\chromedriver_2.29.exe"
  chrome_driver = webdriver.Chrome(binry)
  chrome_driver.get(url_login)

  # Naver Login
  iD = chrome_driver.find_element_by_xpath('//*[@id="id"]')
  iD.send_keys('네이버 아이디')
  psswd = chrome_driver.find_element_by_xpath('//*[@id="pw"]')
  psswd.send_keys('비밀번호')
  login = chrome_driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

  # 댓글 누를 페이지에 접속
  chrome_driver.get(url_hit)

  # 플레이어 끄기
  time.sleep(1)
  ActionChains(chrome_driver).key_down(Keys.SPACE).perform()

  # 연속 재생 끄기
  conti_flag = chrome_driver.find_element_by_xpath('//*[@id="playlistArea"]/div[1]/div/div/a')
  conti_flag.click(); conti_flag.click()

  time.sleep(5)
  # 진짜 웃긴데 창을 전체화면으로 돌려야 찾음.. 왠지 모르겠음 ㅜㅠ
  see_all = chrome_driver.find_element_by_xpath(
                    '//*[@id="cbox_module"]/div/div[5]/div[1]/div/ul/li[2]/a')
  see_all.click() # 전체 댓글 클릭

  time.sleep(1)
  # 팝업 비디오는 꺼주기
  popped_video = chrome_driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[1]/div[1]/a').click()

  local = time.localtime()
  hour = str(local.tm_mon) + "_" + str(local.tm_mday) + "_" \
        + str(local.tm_hour) + "-" + str(local.tm_min)
  page_no = 1
  a_tag_no = 3
  with open("commenters" + hour + ".txt", 'w', encoding="UTF-8") as f:
    while (True): # 돌리고 싶은 페이지 양만큼 돌도록 수정. page_no < 100 처럼
      time.sleep(0.5)

      # page 댓글들
      comments = chrome_driver.find_elements_by_css_selector(
      '#cbox_module > div > div.u_cbox_content_wrap > ul > li.u_cbox_comment')

      for c in comments:
        # 닉네임을 이용해서 자신의 댓글은 패스
        comm_nick = c.find_element_by_xpath('div[1]/div/div[1]/span[1]/span/span/span/span').text
        f.write(comm_nick + "\n")

        if (comm_nick != NICKNAME):
          try:
            like = c.find_elements_by_css_selector('div.u_cbox_comment_box > div > div.u_cbox_tool > div > a.u_cbox_btn_recomm')
          except:  # 경고창이 뜨는 경우
            alert = chrome_driver.switch_to_alert().accept()
            time.sleep(1.5)
            continue
          else:
            if ("u_cbox_btn_recomm_on" not in like[0].get_attribute("class")):
              try:
                like[0].click()
                time.sleep(1)
              except:
                continue

      if (a_tag_no > 7):
        a_tag_no = 3
      next_view = chrome_driver.find_element_by_xpath('//*[@id="cbox_module"]/div/div[7]/div/a[' + str(a_tag_no) + ']').click()

      a_tag_no += 1
      page_no += 1

  chrome_driver.quit()
  f.close()

if __name__ == "__main__":
  main()
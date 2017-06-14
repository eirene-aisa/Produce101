from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import datetime
import re

# Oh Little Girl 최민기 직캠영상 (화면 우측의 재생목록에서 조회수와 하트수 크롤링)
url = "http://tv.naver.com/v/1747159/list/132312"

'''
# GOAL : 
# 몇시간에 한번씩 자동으로 컨셉 평가 직캠 영상 조회수를 멤버별로 기록하는 크롤러

# TODO :
# 1. 한시간에 한번씩 자동으로 실행되서 파일에 쓰기
'''
def main():
  html = urlopen(url).read()
  soup = BeautifulSoup(html, "html.parser")

  # 9 ~ 43번이 연습생 직캠. title + like + hits 포함
  play_list = soup.find_all("div", class_="inner")

  date = datetime.datetime.now().strftime("%Y_%m_%d_%H-%M-%S")
  with open("playLists_" + date + ".txt", "wt", encoding="UTF8") as out:
    for ind in range(9, 44):
      clip = play_list[ind]

      title = clip.find("a", class_="_click thumb")["title"]
      # 공백을 제거한 뒤 multiple delimiter split
      title = re.findall(r"[\w']+", re.sub(r'[ ]+', '', title))
      i = title[2].find("택") # | 문자를 찾고 싶었는데..ㅜㅠ
      trainee = title[2][i + 2:]
      song = title[-2]

      hit = int(clip.find("span", class_="hit").contents[0].replace(',', ''))
      like = int(clip.find("span", class_="like").contents[0].replace(',', ''))

      out.write(trainee + ", " + song + ", "
               + str(hit) + ", " + str(like) + "\n")

  # print("꾸꾸까까?")

if __name__ == "__main__":
  main()
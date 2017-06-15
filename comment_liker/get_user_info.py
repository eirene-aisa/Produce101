from tkinter import *

ID = ""
PSSWD = ""
NICKNAME = ""

def get_user_info():
  content = " *  토끼단을 위해 만들었습니다  *\n" \
          + "인터넷 속도가 어느정도 보장되는 환경에서 사용해주세요.\n\n" \
          + "WARNING :\n" \
          + "네이버 댓글 로딩에 맞추다 보니 빠르지는 않습니다.\n" \
          + "실행이 되면 브라우저 뜬 후 바로 최대화 해주시고요,\n" \
          + "플레이어 정지 -> 연속 재생 해제 후 4초가량 이후\n" \
          + "전체 댓글창 -> 팝업된 비디오를 끄기 이후 좋아요를 누르기 시작합니다.\n"\
          + "실행 중에 클릭을 하면 실행이 멈추고,\n" \
          + "댓글을 누르는 사이사이 스크롤 정도만 허락됩니다ㅜㅠ\n" \
          + "스크롤도 막 하시면 좋아요 누르는 댓글을 건너뛰어요!\n" \
          + "만약 좋아요를 누르기 전에 프로그램이 멈췄다면,\n" \
          + "문의 주시면 느린 인터넷 환경에 맞게 작업해보겠습니다.\n\n" \
          + "프로그램 원본 :\n"\
          + "  https://github.com/dopha-mipa/Produce101/blob/master/comment_liker.py\n" \
          + "  또는 github.com에서 '토끼단' 검색 후 'code' 탭 확인\n" \
          + "개인 정보를 수집하지 않습니다.\n" \
          + "에러 문의 : puremint09@gmail.com\n"

  def setting():
    global ID
    global PSSWD
    global NICKNAME
    
    ID = iD.get()
    PSSWD = pwd.get()
    NICKNAME = nick.get()

    panel.destroy()
    # print(ID, PSSWD, NICKNAME)
    # print("토끼!")

  panel = Tk()
  panel.title("토끼들의 댓글에 하트를 빵빵!")
  Label(panel, text=content).grid(row=0)

  Label(panel, text="Naver ID ").grid(row=1)
  Label(panel, text="password ").grid(row=3)
  Label(panel, text="아이디 별명").grid(row=5)

  iD = Entry(panel)
  iD.grid(row=2)
  pwd = Entry(panel)
  pwd.grid(row=4)
  nick = Entry(panel)
  nick.grid(row=6)
  Label(panel, text="").grid(row=7)

  Button(panel, text="토끼!", command=setting).grid(row=8)

  mainloop()

  # print(ID, PSSWD, NICKNAME)
  return ID, PSSWD, NICKNAME

# if __name__ == "__main__":
#   get_user_info()
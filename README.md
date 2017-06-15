#### for Produce 101 Season 2 video clip on Naver TV  
## crawl_hit_heart - Crawling hits & hearts of video clip

 * /dist  
   To create a windows task schedule (crawl_hitsNLike.py)  
   windows application

 * /playLists  
   result of crawling as playLists_datetime.txt (about every hour)
    data of hits and like of every video  
    (Concept performance - 
    NEVER, 열어줘, Oh Little girl, Show Time, I Know You Know)

 * crawl_hitsNLike.py  
    Crawling hits and like of videos in the NaverTV playlist (beautifulSoup4)  

## comment_liker - Auto 'like' on comments of the video

 * /dist  
   To create a windows task schedule (comment_liker.py)  
   windows application

 * comment_liker.py  
    NaverTv video comments like-clicker (Selenium)  
    (through current ~ the first comment / can be edited.)

 * get_user_info.py  
    code included by comment_liker.py  
    get user Info to log in



### Comment_liker 사용에 관해서  
 (개인정보를 수집하지 않습니다)  

 화면에 보이는 초록색 'Clone or download' 버튼을 눌러 압축 파일을 다운받아주세요.  
 다운 받은 파일의 압축을 해제하시고 나면  
 comment_liker/dist 폴더의 내용을 제외하고는 삭제하셔도 괜찮습니다.  

 dist 폴더 안의 chromedriver_2.29 파일은  
 본인 컴퓨터의 C:\ 폴더로 이동해주세요.  

 dist/comment_liker 폴더 안의 comment_liker.exe를 실행하시면  
 안내창이 나타납니다. 안내창의 내용을 꼭 읽어 주세요!  

 실행에 필요한 정보를 입력한 후 토끼! 를 클릭하시면  
 검은 콘솔창이 뜨고 몇 초 후 크롬이 실행됩니다.
 콘솔창은 최소화 해주시고, 브라우저가 뜨면 바로 창을 최대화 해주세요.  
 액세스 허가를 묻는 창이 나타나면 '예'를 눌러주세요.  

 이후 안내창 내용에 따라 동작하는지 본 동작 시작까지 지켜봐주신 후, 창을 최소화 해두시면 됩니다.

문의 : puremint09@gmail.com
# Thanksgiving-Tetris v2.

추석용 프로젝트: 테트리스를 만들어보자~~ 
실제로 추석에 가족 친구들과 게임 플레이를 하고 피드백을 받으면서 업데이트를 계속 하니 너무 재밌네요^^*
***
### 게임 링크🎮
EC2 배포 링크:
http://3.39.216.163/

이치 링크: 
https://tashahan91.itch.io/thanksgiving-tetris

### 회고 블로그📝
https://velog.io/@tasha_han_1234/%ED%95%AD%ED%95%B4%ED%94%8C%EB%9F%AC%EC%8A%A4-%EC%BD%94%EC%9C%A1%EB%8C%80-%ED%9A%8C%EA%B3%A0-%ED%85%8C%ED%8A%B8%EB%A6%AC%EC%8A%A4%EC%99%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%98-%EA%B0%80%EB%8A%A5%EC%84%B1

![image](https://github.com/Madung2/thanksgiving-tetris/assets/104334219/a19bf9d6-9fb8-401e-8acd-91d5fb3f4700)

### 점수💯
* 아래 방향키로 빨리 내리기 했을 때 : 1점
* 1줄 클리어 했을 때: 100점
* 2줄 동시 클리어 했을 때 : 300점
* 3줄 동시 클리어 했을 때 : 500점
* 4줄 동시 클리어 했을 때 : 800점


### 입력🖊️
* 게임 시작: 오른쪽 스타트 버튼 클릭 or 스페이스바
* 왼쪽으로 이동: 왼쪽 방향키
* 오른쪽으로 이동: 오른쪽 방향키
* 한칸 밑으로 이동: 아래 방향키
* 회전: 위 방향키

### 블록🕹️

* I자형: 4개의 작은 블록이 한 줄로 나열된 모양
* O자형: 4개의 작은 블록이 2x2로 나열된 모양
* T자형: 4개의 작은 블록이 T자형으로 나열된 모양
* L자형: 4개의 작은 블록이 L자형으로 나열된 모양
* J자형: 4개의 작은 블록이 J자형으로 나열된 모양
* S자형: 4개의 작은 블록이 S자형으로 나열된 모양
* z자형: 4개의 작은 블록이 z자형으로 나열된 모양


### 기능💻
1) 그리드
2) 블록
3) 블록 이동
4) 블록 그리드 밖으로 이동 감지
5) 회전
6) 블록 변경 및 이전 블록 고정
7) 한줄 클리어
8) 타이머
9) 완성한 라인 카운드
10) 점수
11) 게임 시작 및 게임오버

### v2 업데이트 기능
12) 스마트폰 플레이 최적화
13) 게임 BGM 추가



### 배포
**로컬테스트**
* async await을 사용해서 게임 루프에 해당하는 main function을 감싸준다
* 게임 루프 하단에 `await asyncio.sleep(0)`를 추가한다. 자세한 설명은 pygbag 깃허브 링크를 참조
* `pip install pygbag` 를 한다
* `pygbag tetris` 명령어를 입력한다. 여기서 tetris는 게임이 있는 디렉토리명이다
* 그럼 /build/web 이라는 디렉토리가 생기는데 이 안에 tetris.apk파일과 index.html favicon 이 생성될 것이다.
* 여기서 index.html은 게임과 연동된 웹페이지 정보이고, tetris.apk는 작성한 pygame정보가 들어있다.
* vscode 라이브서버를 사용해서 이 web 디렉토리에 들어가서 서버를 켜보자. 정상적으로 게임이 브라우저에서 켜진다면 apk와 index.html이 문제 없이 구동되는 것이다.

**서버 실행**
* 사실 이건 클라우드 프론트로 배포해도 아무 문제 없지만 나는 평소 사용하는 EC2서버를 사용했다.
* EC2 서버에 ssh를 사용해서 접근한 뒤에 `sudo apt install nginx` 로 엔지닉스를 설치한다
* `sudo systemctl start nginx` 로 엔지닉스를 시작한다
* git clone으로 web에 해당하는 파일을 서버 안에 클론해둔다 (윈도우에서 SCP사용하기 귀찮아서..)
* nginx는 `/var/www/html` 이라는 폴더 안에 있는 것을 실행한다. 따라서 web파일 안의 컨텐츠를 mv 명령어를 사용해서 해당 디렉토리 안에 넣어둔다.
* 서버의 80번 포트가 열려있는지 다시한번 확인한다
*  끝!!! :-)
### nginx 업데이트를 위한 명령어
sudo mv /home/ubuntu/tetris/tetris/build/web/* /var/www/html/

# Thanksgiving-Tetris

추석용 프로젝트: 테트리스를 만들어보자
***
### 게임 링크
EC2 배포 링크:
http://3.39.216.163/

이치 링크: 
https://tashahan91.itch.io/thanksgiving-tetris

### 회고 블로그
https://velog.io/@tasha_han_1234/%ED%95%AD%ED%95%B4%ED%94%8C%EB%9F%AC%EC%8A%A4-%EC%BD%94%EC%9C%A1%EB%8C%80-%ED%9A%8C%EA%B3%A0-%ED%85%8C%ED%8A%B8%EB%A6%AC%EC%8A%A4%EC%99%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%98-%EA%B0%80%EB%8A%A5%EC%84%B1

### 점수
* 아래 방향키로 빨리 내리기 했을 때 : 1점
* 1줄 클리어 했을 때: 100점
* 2줄 동시 클리어 했을 때 : 300점
* 3줄 동시 클리어 했을 때 : 500점
* 4줄 동시 클리어 했을 때 : 800점


### 입력
* 게임 시작: 오른쪽 스타트 버튼 클릭 or 스페이스바
* 왼쪽으로 이동: 왼쪽 방향키
* 오른쪽으로 이동: 오른쪽 방향키
* 한칸 밑으로 이동: 아래 방향키
* 회전: 위 방향키

### 블록

* I자형: 4개의 작은 블록이 한 줄로 나열된 모양
* O자형: 4개의 작은 블록이 2x2로 나열된 모양
* T자형: 4개의 작은 블록이 T자형으로 나열된 모양
* L자형: 4개의 작은 블록이 L자형으로 나열된 모양
* J자형: 4개의 작은 블록이 J자형으로 나열된 모양
* S자형: 4개의 작은 블록이 S자형으로 나열된 모양
* z자형: 4개의 작은 블록이 z자형으로 나열된 모양


![image](https://github.com/Madung2/thanksgiving-tetris/assets/104334219/a19bf9d6-9fb8-401e-8acd-91d5fb3f4700)


## nginx 업데이트를 위한 명령어
sudo mv /home/ubuntu/tetris/tetris/build/web/* /var/www/html/



# 42메이트

    팀명: 우리사이무슨사이
    프로젝트명: 42mate

# 프로젝트 개요
**하루에 한 번 42분간의 만남을 매칭하는 슬랙봇**

42seoul을 진행하며 학습에 대한 열의와 열린 태도를 가지고 있는 멋진 동료들을 많이 만날 수 있었습니다. 
하지만 다들 모니터를 보느라 바쁘다보니, 서로를 알아갈 계기가 부족한 것이 아쉬웠습니다. 멋진 동료들과 라포가 쌓인다면 상호작용의 질이 향상되지 않을까요?



# 프로젝트 상세
42 mate는 우리의 만남을 장려합니다.
학습에 대한 열의와 열린 태도를 가지고 있는 42서울인들이 더욱 친밀해질 기회를 제공합니다.
슬랙앱을 만듭니다. 하루에 한 번, 42분간의 만남을 매칭합니다.


# 기대성과
42서울인들의 관계자산을 늘림으로써 서로의 학습에 대해 시너지를 주기를 기대합니다.

# We are..

eunhkim 역할: 팀장 / 핵심기여역량: 소스 개발, 프로젝트 관리
jaejeon 역할: 팀원 / 핵심기여역량: 소스 개발, 프로젝트 관리
iwoo 역할: 팀원 / 핵심기여역량: 소스 개발, 프로젝트 관리


# 개발 환경
개발 도구: Python, Flask, Heroku, Postgresql...
협업 도구: Slack, Github, Trello
개발 방식: 밀도 있는 페어 코딩과 코드 리뷰 중심의 협력 개발

# 개발 일지
팀미팅 이후 성과, 이슈, TODO 별로 나눠서 작성

## 2020.04.16

#### 성과
- 프로젝트에서 원하는 것 공유
  - 학습
  - 협업경험
  - 실제 사용가능한 프로덕트
  
- 기획
  - 아이템 선정
    - 42의 학습방식을 비소프트웨어 주제에 적용하는 웹 서비스
    - 42 Slack에서 유용하게 사용할 수 있는 슬랙봇
    - **42 Learner들이 서로를 잘 이해하고, 라포를 쌓을 수 있게하는 서비스/테스트/슬랙봇**
      - 42서울인들의 학습에 도움을 주는 서비스이고, 프로젝트를 만드는 입장에서도 모르던 영역을 배운다는 점에서 도전의식이 생겼음.
    - 기존 시장의 문제들을 해결하는 보드게임 중고거래 서비스
    - C++를 재미있고 쉽게 익힐 수 있는 소프트웨어

- 협업 규칙 협의
    - **비동기적 개발**: 계속 할일을 찾아가며 코드를 개발하는 방식
    - **어떤 함수라도 세 명의 참여 필수**: 팀원이 모두 손을 대어야 우리의 함수이다.
    - **데일리 리뷰 진행**
      - 일시: 매일 오후 13시
      - 내용: 회고, TODO, 논의하고 싶은 사항, 도움 받고 싶은 사항 공유
    - 기타 변경사항은 프로젝트 진행하며 논의 후 추가

- 사용 기술 논의
  - Language: Python 선택. 셋 모두 과거에 진행한 타 프로젝트, '42 AI bootcamp' 등을 통해 파이썬 기초를 접한 상태이고 시간이 제한되어있으니 학습비용이 낮다는 판단.
  - Web framwork: Flask, Django 중 무엇이 적합할지 조사 필요.
  - Database: 무엇이 주로 쓰이는지 확인 필요.
  - Server cloud: AWS, Heroku 등등의 서비스 중 무엇이 적합할지 조사 필요.
  - 그 외 슬랙봇 구현에 필요한 기술이 무엇이 있는지 조사 필요.
  
#### TODO
  - Task list 작성을 위해 아래 두 가지 진행(*아직 뭘 진행해야하는지도 모르는 상태..*)
    - 슬랙봇 작동원리 조사
    - 구현해야할 최소기능 생각
  - 슬랙봇이 42서울 워크스페이스에서 작동가능한지 여부 문의할 것.

## 2020.04.17 ~ 2020.04.19

#### 성과
- 사용할 기술 추가협의
  - Web framwork: Flask
    - 이유: 가벼운 프로젝트를 구현하는데 적합하다고 하고, 필요한 서비스를 직접 연동시키는 경험을 할 수 있기 때문에 학습자에게 적합하다고 함.
  - Database: Postgresql, SQLAlchemy
    - 이유: 둘 모두 참고자료를 찾기 쉬웠음. heroku에서 Postgresql을 연동한 서비스를 제공하고 있고, 주로 SQLAlchemy와 함께 쓰는 것으로 보임.
  - Server cloud: heroku
    - 이유: AWS보다 가볍고 간편하게 cloud서비스를 이용할 수 있어서 작은 규모의 프로젝트를 학습용으로 만드는데 주로 쓰인다고 함.

#### 이슈
 - 앱 토큰을 쓰는 방식과 webhook을 쓰는 방식이 있는 것 같다. 둘 중 하나를 선택 필요
 - 헤로쿠에서 원하는 형태로 DB연동을 시켜야한다.

#### TODO
 - register, unregister, list 확인 명령어를 구현하는 것을 도전

## 2020-04-20

#### 성과
 - 은휼님이 register, unregister, list 확인 명령어를 구현하여 DB연결하는 것을 성공함.

#### 이슈
 - 테스트환경과 배포를 어떻게 할 것인가 논의 필요
    - 방법1: local에서 개발한 것을 ngrok으로 만들고, 슬랙에서 테스트 후 heroku로 올리는 방법
    - 방법2: 앱을 두개 만들어서 하나는 테스트, 하나는 배포용으로 활용
    - 방법3: ngrok을 이용한 테스트봇 3개와 heroku를 이용한 메인 봇을 만들 것.
 - 앱 토큰이 히로쿠로 푸쉬하면 슬랙에서 비활성화되는 문제
    - 서버로 코드를 올리는 과정에서 코드가 public한 공간에 공개되면 앱 토큰이 노출되므로 삭제되는 것으로 추측됨. 
    - private repo에 올려서 되는지 실험해보고 hardcoding된 값들을 환경변수로 감춰서 public repo에 올리면 되는지도 실험해볼 필요가 있음.
    
#### TODO
 - 22일에 오프라인에서 만날 때까지 어떤 식으로 앱을 기획하면 좋을지 구상

## 2020-04-21 ~ 2020-04-22

#### 성과
 - 앱 세부기획 진행
    - user는 42seoul 구성원이며 needs는 1) 학습욕구 2) 소셜욕구를 가지고 있다. 그 중 소셜욕구를 충족시키는 방향으로 결정함. 소셜욕구가 충족되면 학습욕구 해소까지 이어지도록 유도할 수 있을거라고 기대
    - 서비스형태는 1) 정보를 입력받고 2) 하루에 한번 42분간 만날 user를 매칭하고 3) 메세지로 알려주는 형태로 결정
    - 버전별로 구현할 기능과 DB모델 정함. DB모델은 아래와 같음.
        - version 1.0
            - **User 테이블**
                - **Slack_id (프라이머리 키)**
                - **Intra_id**
                - **Register (type: boolean)**
                - **Joined (type: boolean)**
            - **Match 테이블**
                - **Index (프라이머리 키)**
                - **Date_time (type: time)**
                - **User A (slack_id)**
                - **User B (slack_id)**
        - version 2.0
            - User 테이블
                - Slack_id (프라이머리 키)
                - Intra_id
                - Register (type: boolean)
                - Joined (type: boolean)
                - **Noshow_count (type: int)**
                - **Noshow_rate (type: double)**
                - **Satisfy_rate (type: double)**
            - Match 테이블
                - Index (프라이머리 키)
                - Date_time (type: time)
                - User A (slack_id)
                - User B (slack_id)
            - **Eval 테이블**
                - **Index (프라이머리 키)**
                - **Match**
                - **User_from**
                - **User_to**
                - **No_show (boolean)**
                - **Satisfy (double)**
        - version 3.0
            - User 테이블
                - Slack_id (프라이머리 키)
                - Intra_id
                - Register (type: boolean)
                - Joined (type: boolean)
                - Noshow_count (type: int)
                - Noshow_rate (type: double)
                - Satisfy_rate (type: double)
                - **Interest**
            - Match 테이블
                - Index (프라이머리 키)
                - Date_time (type: time)
                - User A (slack_id)
                - User B (slack_id)
                - Eval 테이블
                - Index (프라이머리 키)
                - Match
                - User_from
                - User_to
            - **Interest 테이블**
                - **Index (프라이머리 키)**
                - **Interest**
                - **User**
                - **Question**
                - **Link**
#### TODO
 - 기본이 되는 테스트 슬랙 봇 구현
    - 페어 프로그래밍으로 개발환경과 기본 구현 방식을 동기화

## 2020-04-23

#### 성과

 - **기본 테스트 슬랙봇 구현** <br>
    - 지금까지는 각자 학습을 위해 슬랙봇을 따로 만들어본 상태였음. 본 프로젝트를 위해 개발환경을 동기화하고, 함께 쓸 코드를 작성할 필요를 느꼈고, 각자 페어프로그래밍 방식으로 약 4시간 30분 동안 진행함. 과정은 아래와 같음.
    - **파이참으로 프로젝트 생성**
        - 파이참과 vscode 중 무엇을 쓸지 논의하였고, eunhul님 컴퓨터에서 vscode가 컴퓨터자원을 많이 소모하는 이슈가 있고, 파이참이 파이썬 라이브러리 설치나 가상환경 셋팅 등이 편리한 것 같다는 이유로 파이참을 선택함.
    - **Flask 등 필요한 라이브러리를 설치** 
    - **슬랙앱 생성**
        - 권한 scope 설정하여 slack app token을 발급 받아서 플라스크에 연동시킴.
    - **데이터베이스 생성 및 연동**
        - **user table, match table** 생성
        - primary key가 string보다는 integer 타입으로 관리되는 것이 간편하다고 하여 match table에도 index column을 추가
        - user와 match간의 관계가 ‘many to many’라는 것을 감안하여 **user_identifier table**을 추가함.
    - **Heroku로 배포, 데이터베이스 연동**

#### 이슈
 - match가 생성되었을 때 저장되는 시간 값이 미국 서버 시간 기준으로 저장되는 것으로 보인다. 한국시간으로 바꿔줄 필요가 있다.
 - 프로토타입을 위해 구현하고 처리해야할 기능,이슈들을 트렐로에 정리가 필요하다.

**추가 협의사항**
 - 문자열 사용시 쌍따옴표(“) 활용, key값은 홀따옴표(‘) 활용

#### TODO
 - UI개선을 위해 block-kit 학습

## 2020-04-24

#### 성과
 - 42mate 서비스 이용에 필요한 버튼을 구현하는 것이 command를 이용하는 것보다 유저친화적이라는 판단하에 block kit으로 42mate 커맨드 버튼 뷰를 구현하기로 함.
 - 논의를 바탕으로 42mate 1.0 version을 위해 필요한 task를 정리하여 트렐로에 카드 생성함. 정리한 task는 현재 아래와 같음.
    - 서버 한국시간 설정
    - 42mate 커맨드 버튼 뷰 구현
    - 커맨드 입력값 제어 & 예외처리
    - register 커맨드 구현
    - unregister 커맨드 구현
    - join 커맨드 구현
    - bye 커맨드 구현
    - 매칭 구현
    - 앱 이미지 디자인

#### 이슈
 - develop 브런치를 새로 만들어서 배포 프로젝트와 개발중인 프로젝트를 분리시켜야할 것 같다. 논의하여 진행할 것

#### TODO
 - 각자 원하는 task를 처리할 것

## 2020-04-25

#### 성과
 - match 테이블의 match time 에 저장되는 값을 어떻게 처리할지 정함.
    - UTC 값이 match 테이블에 저장되도록하고, 해당 시간 활용시 localtime으로 변환해서 사용하기로 협의
 - 커맨드 버튼뷰를 구현함.
    - 슬랙 id가 이미 등록되었는지 여부에 따라 register 함수 실행여부를 결정하는 형태까지 구현됨
   - bye로 통칭하던 기능의 이름이 적절하지 않다는 의견에 따라 unjoin으로 기능의 이름을 변경
 - 하나의 작업을 혼자서 모두 하지 않는다!는 원칙하에 협업방식 세부설정
    - 카드 사이즈가 크면 체크리스트를 쪼개가면서 설정한다. 이를 위해 원래 작업하시던 분에게는 체크리스트를 요청해야함.
    - 그럼 체크리스트를 완료했다면? 로컬에서 원래 작업자의 branch로 pull request를 날린다.
    - 혼자 하더라도 팀미팅시 코드 공유해서 모든 팀원에게 학습이 일어나야한다.
    
#### 이슈
 - 커맨드 뷰에서 유저의 상태에 따라 보여주는 버튼뷰가 달라져야함.
 - 깃헙 브랜치들을 정리 필요. 특히 누군가가 작업 중인 task에 어떻게 참여할지 방식 협의 필요.
    - 밋업에서 지금까지 한 것을 또 푸쉬하고, 필요한 것을 수정한다. 이후 각자의 브런치에 만든 기능을 만든다음에 dev에 pull request해서 리뷰를 거쳐서 둘 중 하나를 merge한다.
    - 로컬에서는 트렐로 카드별로 로컬브랜치가 따로 있어야함.

#### TODO
 - 스케쥴  포함해서 매칭 함수 구현
 - 커맨드뷰 구현 위해 시나리오 작성
 - 우선 attachment가 하드코딩되어있다는 가정하에 커맨드뷰 코드 구현
 - get_attachments 함수 구현 시작

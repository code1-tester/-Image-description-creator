# 팀원
#### 202434856 최하진 UI 제작
#### 202434833 정재형 데이터 수집
#### 202434857 최훈  코드 작성 
#### 202434847 주수하 팀 리더 및 코드 작성

### ImageNarrator

프로젝트 개요

이 프로젝트는 이미지에서 핵심 정보를 추출하고 자연어로 설명을 생성하는 오픈소스 소프트웨어입니다. 사용자는 이미지를 GUI를 통해 입력하면 해당 이미지의 내용을 자동으로 분석하고 적절한 언어로 텍스트를 생성할 수 있습니다.

주요 기능: 이미지 분석, 객체 감지, 자연어 생성.
적용 사례: 데이터 세트의 자동 태그 생성, 시각 자료를 위한 콘텐츠 생성 자동화.
특징: 사용이 간편한 API, 다국어 지원, 높은 커스터마이징 가능성.
이 프로젝트는 이미지와 텍스트의 연결을 통해 접근성을 향상시키고 콘텐츠 제작 효율성을 높이는 데 기여하고자 합니다.

만드는 데에 사용된 소스

Salesforce/blip-image-captioning-base
https://huggingface.co/Salesforce/blip-image-captioning-base

설치 필요 

pip install googletrans==4.0.0-rc1

실행 방법

본인의 운영체제에 맞는 OSS_GUI.py 파일을 선택하고 실행한다. 이후 upload image를 눌러 이미지를 선택한다.

##### 첫 번째 이미지(코드 실행 후 화면)
![스크린샷 1](https://github.com/code1-tester/Image-description-creator/blob/main/result_collection/using_image1.png)
##### 두 번째 이미지(파일 업로드 눌렀을 때 화면)
![스크린샷 2](https://github.com/code1-tester/Image-description-creator/blob/main/result_collection/using_image2.png
)
##### 세 번째 이미지(예시 사진:자전거)
![스크린샷 3](https://github.com/code1-tester/Image-description-creator/blob/main/result_collection/using_image3.png
)
##### 네 번째 이미지(예시 사진:도서관)
![스크린샷 4](https://github.com/code1-tester/Image-description-creator/blob/main/result_collection/using_image4.png)
##### 다섯 번째 이미지(예시 사진:말)
![스크린샷 5](https://github.com/code1-tester/Image-description-creator/blob/main/result_collection/using_image5.png)
##### 여섯 번째 이미지(예시 사진:고양이)
![스크린샷 6](https://github.com/code1-tester/Image-description-creator/blob/main/result_collection/using_image6.png)




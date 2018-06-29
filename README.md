# PyExcelToBSON

단일 `Excel(xlsx) File`에 대하여 `Sheet`별로 `BSON(Binary JSON)`으로 변환하는 Python Script

## 용도

개인적인 프로젝트에 쓰기 위한 스크립트이다. 어떠한 환경에서도 돌아가게 하기 위해 만들었다.

```Excel```에 미리 정의된 Data Model을 ```BSON```으로 생성해준다.

## 구동환경

- `Python 3.5` 이상이 동작하는 모든 OS
- [`pipenv`](https://docs.pipenv.org/)로 쉽게 설정 가능

### 의존성 도구들

`pipenv`설정 파일인 `Pipfile`에 의존성 패키지들이 기록되어 있다.

- [`xlrd`](https://github.com/python-excel/xlrd): `Excel`을 불러오는 데 쓰임
- [`bson`](https://github.com/py-bson/bson): `BSON`을 다루는 데 쓰임

## 설치

`Python 3.5` 이상 버전을 설치 후, 아래 구문을 실행한다.

> ```$ pipenv install```

## Excel Sheet 규칙

1. `Sheet` 이름의 맨 앞 글자에 ```_```가 들어가는 경우 DB에 삽입되지 않음.

- 예) ```_info```

2. Sheet에서 1~5번행은 항상 지켜져야 함.

> 2번의 경우에는 추후 추가될 `PyExcelToCS`에 필요한 규칙이므로 그대로 따라간다.

- 1번행: 해당 열에 대한 설명
- 2번행: 해당 열의 용도 (사용되지 않을 예정)
- 3번행: 해당 열의 Attribute
- 4번행: 해당 열의 Data Type
- 5번행: 해당 열의 이름 (변수명)

3. 내부 데이터 값은 비어있지 않아야 함.

## 사용법

```$ PyExcelToBSON.py -i sample.xlsx```

1. ```sample.xlsx```와 같은 형식의 Excel(xlsx) 파일을 준비한다. (Repository에 있음)

2. 적절한 인자 값을 넣고 ```PyExcelToBSON.py```을 실행한다. 인자를 넣는 순서는 상관없다.

- ```-i```, ```--input```: Excel(xlsx) 경로와 파일 이름
- ```-d```, ```--debug```: JSON 파일로 Export
- ```-c```, ```--clean```: `output`폴더 정리

3. `output`폴더에 나온 결과물을 확인한다.

> 결과물은 `data`에 배열로 들어가는 형태로 구성되어 있다.

## 해야할 일

- 코드 리펙토링
- (가능하면) Google Sheet 연동

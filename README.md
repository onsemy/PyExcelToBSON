# PyExcelToBSON

단일 `Excel(xlsx) File`에 대하여 `Sheet`별로 `BSON(Binary JSON)`으로 변환하는 Python Script

## 이것은 무엇인가요?

개인적인 프로젝트에 쓰기 위한 스크립트입니다. 어떠한 환경에서도 돌아가게 하기 위해 만들었다.

```Excel```에 미리 정의된 Data Model을 ```BSON```으로 생성해준다.

## 어떤 일을 하나요?

단일 `Excel(xlsx) File`에 대하여 `Sheet`별로 `BSON(Binary JSON)`으로 변환합니다.

## 무엇이 필요한가요?

- [`python3.7`](https://www.python.org/downloads/): PyExcelToBSON은 *Python 3*를 기반으로 만들어집니다.
- [`virtualenv`](https://virtualenv.pypa.io/en/stable/): 독립적인 개발 환경을 지원합니다.
- [`openpyxl`](https://openpyxl.readthedocs.io/en/stable/): Excel을 다루기 위해서 필요합니다.
- [`bson`](https://github.com/py-bson/bson): BSON을 다루기 위해서 필요합니다.

## 어떻게 개발하나요?

1. *python 3.7*을 설치합니다. Windows에서 설치 시, Add to PATH를 활성화하여 설치합니다.
2. `git clone https://github.com/onsemy/PyExcelToBSON.git` 또는 `git clone git@github.com:onsemy/PyExcelToBSON.git`으로 Project를 내려 받습니다.
3. `pip install virtualenv`로 `virtualenv`를 설치합니다.
4. `PyExcelToBSON` Directory로 이동하여 Project에 대한 가상 환경을 구축합니다.
  > Windows의 경우 `virtualenv venv`를 실행합니다.
  > Mac의 경우 `virtualenv -p python3 venv`를 실행합니다.
5. 가상 환경을 실행합니다.

 OS | 활성화 | 비활성화 
---|-------|-------
Windows | `\venv\Scripts\activate.bat` | `deactivate.bat`
Mac | `source venv/bin/activate` | `deactivate`

6. `pip install -r requirements.txt`로 의존성 Package를 가상 환경에 구축합니다.
7. 개발을 시작합니다.

## 어떻게 사용하나요?

### Excel Sheet 규칙

1. `Sheet` 이름의 맨 앞 글자에 ```_```가 들어가는 경우 BSON으로 내보내지지 않습니다.

- 예) ```_info```

2. Sheet에서 1~5번행은 항상 아래와 같이 지켜져야 합니다.

> 2번의 경우에는 [`PyExcelToMustache`](https://github.com/onsemy/PyExcelToMustache)에 필요한 규칙이므로 그대로 따라간다.

- 1번행: 해당 열에 대한 설명
- 2번행: 해당 열의 용도 (사용되지 않을 예정)
- 3번행: 해당 열의 Attribute
- 4번행: 해당 열의 Data Type
- 5번행: 해당 열의 이름 (변수명)

3. 내부 데이터 값은 비어있지 않아야 합니다.

### 사용법

```$ PyExcelToBSON.py -i sample.xlsx```

1. ```sample.xlsx```와 같은 형식의 Excel(xlsx) 파일을 준비합니다. (Sample이 Repository에 포함되어 있음)

2. 적절한 인자 값을 넣고 ```PyExcelToBSON.py```을 실행합니다. 인자를 넣는 순서는 상관없습니다.

- ```-i```, ```--input```: Excel(xlsx) 경로와 파일 이름. **실행 시 반드시 입력해야 합니다.**
- ```-o```, ```--output```: 결과가 출력될 폴더 경로. **실행 시 반드시 입력해야 합니다.**
- ```-d```, ```--debug```: JSON 파일로 Export
- ```-c```, ```--clean```: `output`폴더 정리
- ```-s```, ```--suffix```: 결과물의 접미사

3. `output`폴더에 나온 결과물을 확인합니다.

> 결과물은 `data`에 배열로 들어가는 형태로 구성되어 있습니다.

## 남은 일은 무엇인가요?

- 코드 리펙토링
- (가능하면) Google Sheet 연동

## 기여 또는 문의 사항

[`Issue Board`](https://github.com/Game-Pocket/Friday/issues) 혹은 [`email`](mailto:onsemy@gmail.com)로 문의해주세요!

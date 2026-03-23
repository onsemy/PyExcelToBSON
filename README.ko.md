# PyExcelToBSON

> 🇺🇸 [English Documentation](README.md)

Excel (`.xlsx`) 파일의 각 시트를 **BSON (Binary JSON)** 파일로 변환하는 CLI 도구입니다.

## 필요한 것들

- Python `>= 3.6`
- [`openpyxl`](https://openpyxl.readthedocs.io/en/stable/): Excel 파일 읽기
- [`bson`](https://github.com/py-bson/bson): BSON 직렬화

## 설치

```bash
pip install pyexcel2bson
```

## 사용법

```bash
pyexcel2bson -i sample.xlsx -o ./output
```

### 인자

| 인자 | 설명 | 필수 여부 |
|---|---|---|
| `-i`, `--input` | Excel (`.xlsx`) 파일 경로 | ✅ |
| `-o`, `--output` | 출력 디렉토리 경로 | ✅ |
| `-s`, `--suffix` | 출력 파일명 접미사 | ❌ |
| `-d`, `--debug` | JSON 파일도 함께 출력 (디버그용) | ❌ |
| `-c`, `--clean` | 변환 전 출력 디렉토리 초기화 | ❌ |

### Excel 시트 규칙

1. 이름이 `_`로 시작하는 시트는 건너뜁니다.
   - 예) `_info`

2. 1~5행은 아래 구조를 따라야 합니다:

| 행 | 설명 |
|---|---|
| 1 | 해당 열에 대한 설명 |
| 2 | 해당 열의 용도 (예약됨) |
| 3 | 해당 열의 Attribute |
| 4 | 해당 열의 Data Type |
| 5 | 해당 열의 이름 (변수명) |

3. 데이터 셀은 비어 있으면 안 됩니다.

### 출력 형식

각 시트는 아래 구조의 `.bson` 파일로 출력됩니다:

```json
{
  "data": [
    { "column_name": value, ... },
    ...
  ]
}
```

## 개발 환경 구축

```bash
git clone https://github.com/onsemy/PyExcelToBSON.git
cd PyExcelToBSON
pip install -e ".[dev]"
```

## 프로젝트 구조

```
PyExcelToBSON/
├── main.py
├── output_manager.py
├── readers/
│   ├── input_reader.py    # 추상 기반 클래스
│   └── excel_reader.py
├── writers/
│   ├── output_writer.py   # 추상 기반 클래스
│   ├── bson_writer.py
│   └── json_writer.py
└── factories/
    ├── reader_factory.py
    └── writer_factory.py
```

## 기여 또는 문의

[Issue Board](https://github.com/onsemy/PyExcelToBSON/issues) 혹은 [이메일](mailto:onsemy@gmail.com)로 문의해주세요.
# PyExcelToBSON

> 🇰🇷 [한국어 문서](README.ko.md)

A CLI tool that converts each sheet of an Excel (`.xlsx`) file into a **BSON (Binary JSON)** file.

## Requirements

- Python `>= 3.6`
- [`openpyxl`](https://openpyxl.readthedocs.io/en/stable/): For reading Excel files
- [`pymongo`](https://pymongo.readthedocs.io/): For BSON serialization (includes `bson` module)

## Installation

```bash
pip install pyexcel2bson
```

## Usage

```bash
pyexcel2bson -i sample.xlsx -o ./output
```

### Arguments

| Argument | Description | Required |
|---|---|---|
| `-i`, `--input` | Path to the Excel (`.xlsx`) file | ✅ |
| `-o`, `--output` | Path to the output directory | ✅ |
| `-s`, `--suffix` | Suffix appended to output filenames | ❌ |
| `-d`, `--debug` | Also export as JSON for debugging | ❌ |
| `-c`, `--clean` | Clean up the output directory before converting | ❌ |

### Excel Sheet Rules

1. Sheets whose name starts with `_` are skipped.
   - e.g. `_info`

2. Rows 1–5 must follow this structure:

| Row | Description |
|---|---|
| 1 | Column description |
| 2 | Column usage (reserved) |
| 3 | Column attribute |
| 4 | Column data type |
| 5 | Column name (variable name) |

3. Data cells must not be empty.

### Output Format

Each sheet is exported as a `.bson` file with the following structure:

```json
{
  "data": [
    { "column_name": value, ... },
    ...
  ]
}
```

## Development

```bash
git clone https://github.com/onsemy/PyExcelToBSON.git
cd PyExcelToBSON
pip install -e ".[dev]"
```

## Project Structure

```
PyExcelToBSON/
├── main.py
├── output_manager.py
├── readers/
│   ├── input_reader.py    # Abstract base class
│   └── excel_reader.py
├── writers/
│   ├── output_writer.py   # Abstract base class
│   ├── bson_writer.py
│   └── json_writer.py
└── factories/
    ├── reader_factory.py
    └── writer_factory.py
```

## Contributing

Please open an [Issue](https://github.com/onsemy/PyExcelToBSON/issues) or send an [email](mailto:onsemy@gmail.com).
# Лабораторная работа №6 (CLI-утилиты с argparse)

## Описание
В рамках работы созданы консольные утилиты (CLI) с использованием стандартной библиотеки `argparse`. Программа поддерживает подкоманды, флаги и обработку ошибок.

## Команды

### 1. Утилита для работы с текстом (`cli_text.py`)
Реализованы подкоманды `cat` и `stats` (используют функции из ЛР3).

**Вывод файла с нумерацией строк:**
python src/lab06/cli_text.py cat --input data/samples/people.txt -n

**Анализ частот слов (Топ-N):**
python src/lab06/cli_text.py stats --input data/samples/people.txt --top 3

### 2. Конвертеры данных (`cli_convert.py`)
Оборачивают функции из ЛР5 для конвертации форматов.

**JSON в CSV:**
python src/lab06/cli_convert.py json2csv --in data/samples/people.json --out data/out/people_cli.csv

**CSV в JSON:**
python src/lab06/cli_convert.py csv2json --in data/samples/people.csv --out data/out/people_cli.json

**CSV в XLSX:**
python src/lab06/cli_convert.py csv2xlsx --in data/samples/people.csv --out data/out/people_cli.xlsx

## Валидация и справка
- Каждая команда и подкоманда поддерживает флаг `--help` для вывода справки.
- Если входной файл не найден, выводится сообщение об ошибке через `parser.error(...)`.
- Код использует только стандартную библиотеку.

## Примеры вывода (скриншоты)

Справка CLI

<img width="895" height="363" alt="image" src="https://github.com/user-attachments/assets/78eb9be9-6814-4047-9efa-bd67e6186720" />

Работа команды stats

<img width="907" height="214" alt="image" src="https://github.com/user-attachments/assets/0077f212-868e-4f93-a559-b0cf345f7ebc" />

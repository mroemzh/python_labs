import argparse
import sys
from pathlib import Path

# Подключаем корень проекта, чтобы импорты работали
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main():
    # Создаем главный парсер
    parser = argparse.ArgumentParser(description="Конвертеры данных (JSON, CSV, XLSX)")
    
    # Создаем подкоманды
    subparsers = parser.add_subparsers(dest="command", required=True, help="Доступные команды")

    # 1. Команда json2csv
    parser_j2c = subparsers.add_parser("json2csv", help="Конвертировать JSON в CSV")
    parser_j2c.add_argument("--in", dest="input", required=True, help="Путь к входному JSON")
    parser_j2c.add_argument("--out", dest="output", required=True, help="Путь к выходному CSV")

    # 2. Команда csv2json
    parser_c2j = subparsers.add_parser("csv2json", help="Конвертировать CSV в JSON")
    parser_c2j.add_argument("--in", dest="input", required=True, help="Путь к входному CSV")
    parser_c2j.add_argument("--out", dest="output", required=True, help="Путь к выходному JSON")

    # 3. Команда csv2xlsx
    parser_c2x = subparsers.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX")
    parser_c2x.add_argument("--in", dest="input", required=True, help="Путь к входному CSV")
    parser_c2x.add_argument("--out", dest="output", required=True, help="Путь к выходному XLSX")

    # Читаем аргументы
    args = parser.parse_args()

    # Вызываем нужную функцию в зависимости от команды
    try:
        if args.command == "json2csv":
            json_to_csv(args.input, args.output)
            print(f"Успех: {args.input} -> {args.output}")
            
        elif args.command == "csv2json":
            csv_to_json(args.input, args.output)
            print(f"Успех: {args.input} -> {args.output}")
            
        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
            print(f"Успех: {args.input} -> {args.output}")
            
    except FileNotFoundError:
        # Выводим понятную ошибку через argparse
        parser.error(f"Файл не найден: {args.input}")
    except ValueError as e:
        parser.error(f"Ошибка данных: {e}")
    except Exception as e:
        parser.error(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
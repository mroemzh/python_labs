import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """Преобразует JSON-файл в CSV.
    
    Поддерживает список словарей [{...}, {...}].
    Заполняет отсутствующие поля пустыми строками.
    """
    p_in = Path(json_path)
    p_out = Path(csv_path)

    # Проверка на существование файла (FileNotFoundError выбросится сам при .open)
    with p_in.open("r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON или неподдерживаемая структура")

    # Валидация структуры
    if not isinstance(data, list) or not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Список должен содержать только объекты (словари)")

    # Собираем все уникальные ключи (колонки), сохраняя порядок
    fieldnames = []
    for item in data:
        for key in item.keys():
            if key not in fieldnames:
                fieldnames.append(key)

    # Создаем родительские папки, если их нет (на всякий случай)
    p_out.parent.mkdir(parents=True, exist_ok=True)

    # Записываем в CSV
    with p_out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            # Если в словаре нет какого-то ключа, DictWriter запишет пустую строку
            # Но мы можем сделать это явно, на всякий случай
            clean_row = {k: row.get(k, "") for k in fieldnames}
            writer.writerow(clean_row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """Преобразует CSV в JSON (список словарей).
    
    Заголовок обязателен, значения сохраняются как строки.
    """
    p_in = Path(csv_path)
    p_out = Path(json_path)

    # Проверка на существование файла
    with p_in.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        # Проверка, что заголовок есть
        if not reader.fieldnames:
            raise ValueError("CSV без заголовка или пустой")
            
        data = list(reader)

    if not data:
        raise ValueError("CSV без заголовка или пустой")

    p_out.parent.mkdir(parents=True, exist_ok=True)

    # Записываем в JSON
    with p_out.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    print("--- ТЕСТ 1: Успешная конвертация ---")
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    print("OK: JSON -> CSV\n")

    print("--- ТЕСТ 2: Ошибка FileNotFoundError (нет файла) ---")
    try:
        json_to_csv("data/samples/no_such_file.json", "data/out/err.csv")
    except FileNotFoundError as e:
        print(f"УСПЕШНО ПОЙМАНА ОШИБКА: {e}\n")

    print("--- ТЕСТ 3: Ошибка ValueError (пустой JSON) ---")
    # Создаем пустой файл для теста
    empty_path = Path("data/samples/empty.json")
    empty_path.parent.mkdir(parents=True, exist_ok=True)
    empty_path.write_text("[]", encoding="utf-8")
    
    try:
        json_to_csv(empty_path, "data/out/err.csv")
    except ValueError as e:
        print(f"УСПЕШНО ПОЙМАНА ОШИБКА: {e}\n")
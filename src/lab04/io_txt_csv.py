import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает текстовый файл целиком и возвращает строку.
    
    Если файл не найден, поднимает FileNotFoundError.
    Если кодировка не подходит, поднимает UnicodeDecodeError.
    Для чтения в другой кодировке передайте аргумент, например encoding="cp1251".
    """
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(
    rows: list[tuple | list], 
    path: str | Path, 
    header: tuple[str, ...] | None = None
) -> None:
    """Записывает данные в CSV файл.
    
    Если передан header, он пишется первой строкой.
    Проверяет, что все строки в rows имеют одинаковую длину.
    """
    p = Path(path)
    
    # Проверка на одинаковую длину строк
    if rows:
        expected_len = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != expected_len:
                raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидалась {expected_len}")

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


def ensure_parent_dir(path: str | Path) -> None:
    """Создаёт родительские директории для указанного пути, если их нет."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

import sys
import argparse
from pathlib import Path
from collections import Counter

# Добавляем корень проекта в sys.path, чтобы импортировать lib.text
sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.text import normalize, tokenize, top_n
from lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir


def frequencies_from_text(text: str) -> dict[str, int]:
    """Нормализует текст, токенизирует и считает частоты."""
    tokens = tokenize(normalize(text))
    return Counter(tokens)


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Сортирует пары (слово, частота) по убыванию частоты, затем по алфавиту."""
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def main() -> None:
    parser = argparse.ArgumentParser(description="Генерирует статистику по тексту.")
    parser.add_argument("--in", dest="input_file", default="data/lab04/input.txt", help="Путь к входному файлу")
    parser.add_argument("--out", dest="output_file", default="data/lab04/report.csv", help="Путь к CSV отчёту")
    parser.add_argument("--encoding", default="utf-8", help="Кодировка файла")
    args = parser.parse_args()

    try:
        raw_text = read_text(args.input_file, encoding=args.encoding)
    except FileNotFoundError:
        print(f"Ошибка: файл {args.input_file} не найден.")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Ошибка: не удалось прочитать {args.input_file} в кодировке {args.encoding}.")
        sys.exit(1)

    freq = frequencies_from_text(raw_text)
    sorted_counts = sorted_word_counts(freq)

    # Вывод в консоль
    total_tokens = sum(freq.values())
    unique_tokens = len(freq)

    print(f"Всего слов: {total_tokens}")
    print(f"Уникальных слов: {unique_tokens}")
    print("Топ-5:")
    for word, cnt in top_n(freq, 5):
        print(f"{word}:{cnt}")

    # Запись в CSV
    ensure_parent_dir(args.output_file)
    
    if not sorted_counts:
        # Если файл пустой, пишем только заголовок (как рекомендовано в задании)
        write_csv([], args.output_file, header=("word", "count"))
    else:
        write_csv(sorted_counts, args.output_file, header=("word", "count"))

    print(f"\nОтчёт сохранён в {args.output_file}")


if __name__ == "__main__":
    main()
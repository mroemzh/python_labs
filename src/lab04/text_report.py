import sys
import argparse
from pathlib import Path
from collections import Counter

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
    
    # Меняем аргумент --in на nargs="+", чтобы принимать список файлов
    parser.add_argument("--in", dest="input_files", nargs="+", default=["data/lab04/input.txt"], help="Путь(и) к входным файлам")
    
    # Аргументы для звездочки
    parser.add_argument("--per-file", dest="per_file_out", help="Путь для сохранения отчета по каждому файлу (со звездочкой)")
    parser.add_argument("--total", dest="total_out", help="Путь для сохранения общего отчета (со звездочкой)")
    
    # Для базовой версии
    parser.add_argument("--out", dest="output_file", default="data/lab04/report.csv", help="Путь к базовому CSV отчёту")
    parser.add_argument("--encoding", default="utf-8", help="Кодировка файла")
    
    args = parser.parse_args()

    total_freq = Counter()
    per_file_rows = []

    # 1. Обрабатываем каждый файл
    for filepath in args.input_files:
        try:
            raw_text = read_text(filepath, encoding=args.encoding)
        except FileNotFoundError:
            print(f"Ошибка: файл {filepath} не найден.")
            sys.exit(1)
        except UnicodeDecodeError:
            print(f"Ошибка: не удалось прочитать {filepath} в кодировке {args.encoding}.")
            sys.exit(1)

        freq = frequencies_from_text(raw_text)
        total_freq.update(freq) # Добавляем в общую копилку

        # Если нужен отчет по файлам (звездочка)
        if args.per_file_out:
            # Берем только имя файла (без пути), как в примере: a.txt, b.txt
            filename = Path(filepath).name
            for word, cnt in sorted_word_counts(freq):
                per_file_rows.append((filename, word, cnt))

    # 2. Вывод в консоль (по общему количеству)
    total_tokens = sum(total_freq.values())
    unique_tokens = len(total_freq)

    print(f"Всего слов: {total_tokens}")
    print(f"Уникальных слов: {unique_tokens}")
    print("Топ-5:")
    for word, cnt in top_n(total_freq, 5):
        print(f"{word}:{cnt}")

    # 3. Запись базового отчета (report.csv)
    if args.output_file:
        ensure_parent_dir(args.output_file)
        sorted_counts = sorted_word_counts(total_freq)
        if not sorted_counts:
            write_csv([], args.output_file, header=("word", "count"))
        else:
            write_csv(sorted_counts, args.output_file, header=("word", "count"))
        print(f"\nБазовый отчёт сохранён в {args.output_file}")

    # 4. Запись отчета по файлам (report_per_file.csv) - ЗВЕЗДОЧКА
    if args.per_file_out:
        ensure_parent_dir(args.per_file_out)
        # Сортируем по файлу (A-Z), потом по частоте (убывание), потом по слову
        per_file_rows.sort(key=lambda r: (r[0], -r[2], r[1]))
        write_csv(per_file_rows, args.per_file_out, header=("file", "word", "count"))
        print(f"Отчёт по файлам сохранён в {args.per_file_out}")

    # 5. Запись общего отчета (report_total.csv) - ЗВЕЗДОЧКА
    if args.total_out:
        ensure_parent_dir(args.total_out)
        sorted_counts = sorted_word_counts(total_freq)
        if not sorted_counts:
            write_csv([], args.total_out, header=("word", "count"))
        else:
            write_csv(sorted_counts, args.total_out, header=("word", "count"))
        print(f"Общий отчёт сохранён в {args.total_out}")


if __name__ == "__main__":
    main()
import argparse
import sys
from pathlib import Path

# Подключаем корень проекта
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Импортируем функции из ЛР3
from src.lib.text import normalize, tokenize, count_freq, top_n

def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты для текста")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Доступные команды")

    # 1. Команда cat
    parser_cat = subparsers.add_parser("cat", help="Вывести содержимое файла")
    parser_cat.add_argument("--input", required=True, help="Путь к файлу")
    parser_cat.add_argument("-n", action="store_true", help="Нумеровать строки")

    # 2. Команда stats
    parser_stats = subparsers.add_parser("stats", help="Анализ частот слов в тексте")
    parser_stats.add_argument("--input", required=True, help="Путь к файлу")
    parser_stats.add_argument("--top", type=int, default=5, help="Сколько топ-слов вывести (по умолчанию 5)")

    args = parser.parse_args()

    # Обработка команды cat
    if args.command == "cat":
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                if args.n:
                    for i, line in enumerate(f, start=1):
                        print(f"{i:4d} | {line}", end="")
                else:
                    print(f.read(), end="")
        except FileNotFoundError:
            parser.error(f"Файл не найден: {args.input}")

    # Обработка команды stats
    elif args.command == "stats":
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                text = f.read()
            
            # Используем функции из ЛР3
            norm_text = normalize(text)
            tokens = tokenize(norm_text)
            freq = count_freq(tokens)
            top_words = top_n(freq, n=args.top)

            print(f"Всего слов: {len(tokens)}")
            print(f"Уникальных слов: {len(freq)}")
            print(f"Топ-{args.top}:")
            for word, cnt in top_words:
                print(f"  {word}: {cnt}")

        except FileNotFoundError:
            parser.error(f"Файл не найден: {args.input}")

if __name__ == "__main__":
    main()
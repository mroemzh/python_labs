import csv
import timeit
import sys
from pathlib import Path

# Импортируем наши функции и функцию записи из ЛР4
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab04.io_txt_csv import write_csv


def read_numbers(n: int) -> list:
    """Читает список чисел из CSV-файла."""
    path = f"data/lab07/numbers_{n}.csv"
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [int(row["value"]) for row in reader]


def bench_sorts():
    """Замеряет время работы сортировок."""
    rows = []
    for n in [1000, 10000, 100000]:
        data = read_numbers(n)
        
        # Замеряем встроенный sorted
        t_sorted = timeit.timeit(lambda: sorted(data), number=1)
        rows.append(("sort", n, "sorted", round(t_sorted, 4)))
        
        # На 100 000 квадратичные сортировки могут занять часы!
        # Поэтому ограничиваем их до 10 000
        if n <= 10000:
            t_bubble = timeit.timeit(lambda: bubble_sort(data), number=1)
            rows.append(("sort", n, "bubble", round(t_bubble, 4)))
            
            t_insert = timeit.timeit(lambda: insertion_sort(data), number=1)
            rows.append(("sort", n, "insertion", round(t_insert, 4)))
            
            t_select = timeit.timeit(lambda: selection_sort(data), number=1)
            rows.append(("sort", n, "selection", round(t_select, 4)))
        else:
            # Для 100 000 ставим заглушку, как разрешено в ТЗ
            rows.append(("sort", n, "bubble", "> 60"))
            rows.append(("sort", n, "insertion", "> 60"))
            rows.append(("sort", n, "selection", "> 60"))
            
    return rows


def bench_search():
    """Замеряет время поиска (10 000 запросов к списку из 100 000)."""
    rows = []
    data = read_numbers(100000)
    queries = data[:10000] # Берем первые 10 000 элементов как запросы
    
    # Линейный поиск
    t_linear = timeit.timeit(lambda: [linear_search(data, q) for q in queries], number=1)
    rows.append(("search", 100000, "linear", round(t_linear, 4)))
    
    # Бинарный поиск (сначала сортируем!)
    sorted_data = sorted(data)
    t_bin = timeit.timeit(lambda: [binary_search(sorted_data, q) for q in queries], number=1)
    rows.append(("search", 100000, "binary", round(t_bin, 4)))
    
    return rows


def bench_two_sum():
    """Замеряет время Two Sum."""
    rows = []
    for n in [1000, 10000]:
        data = read_numbers(n)
        # Гарантируем, что target существует
        target = data[0] + data[1] 
        
        t_brute = timeit.timeit(lambda: two_sum_brute(data, target), number=1)
        rows.append(("two_sum", n, "brute", round(t_brute, 4)))
        
        t_fast = timeit.timeit(lambda: two_sum_fast(data, target), number=1)
        rows.append(("two_sum", n, "fast", round(t_fast, 4)))
        
    return rows


if __name__ == "__main__":
    print("Начинаем замеры (это может занять минуту)...")
    
    all_rows = []
    all_rows.extend(bench_sorts())
    all_rows.extend(bench_search())
    all_rows.extend(bench_two_sum())
    
    # Выводим в консоль красивой таблицей
    print(f"{'Task':<10} | {'N':<8} | {'Impl':<10} | {'Seconds':<8}")
    print("-" * 45)
    for row in all_rows:
        print(f"{row[0]:<10} | {row[1]:<8} | {row[2]:<10} | {row[3]:<8}")
        
    # Записываем в CSV (используем функцию из ЛР4)
    write_csv(all_rows, "data/lab07/bench.csv", header=("task", "n", "impl", "seconds"))
    print("\nРезультаты сохранены в data/lab07/bench.csv")
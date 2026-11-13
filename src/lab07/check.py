import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast


def check_sorting(fn, trials=100):
    """Сравнивает fn(nums) со sorted(nums) на случайных данных."""
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        
        result = fn(nums)
        
        # Проверяем, что отсортировали правильно
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result} != {sorted(nums)}"
        # Проверяем, что исходный список не изменился
        assert nums == original, f"{fn.__name__} изменила исходный список {original} -> {nums}"


def check_search():
    """Сравнивает linear_search и binary_search с list.index."""
    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        
        # Проверяем линейный поиск
        x = random.randint(-100, 100)
        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1
            
        result = linear_search(nums, x)
        assert result == expected, f"linear_search ошибся на {nums} для {x}: {result} != {expected}"
        
        # Проверяем бинарный поиск (на отсортированном списке!)
        sorted_nums = sorted(nums)
        result_bin = binary_search(sorted_nums, x)
        
        if x in sorted_nums:
            # Если элемент есть, главное, чтобы индекс указывал на него (а не на другое число)
            assert sorted_nums[result_bin] == x, f"binary_search ошибся на {sorted_nums} для {x}: вернул индекс {result_bin}, но там {sorted_nums[result_bin]}"
        else:
            # Если элемента нет, должен вернуть -1
            assert result_bin == -1, f"binary_search ошибся на {sorted_nums} для {x}: вернул {result_bin}, ожидалось -1"

def check_two_sum(trials=100):
    """Сравнивает оба two_sum между собой."""
    for _ in range(trials):
        n = random.randint(0, 30)
        nums = [random.randint(-50, 50) for _ in range(n)]
        target = random.randint(-100, 100)
        
        res_brute = two_sum_brute(nums, target)
        res_fast = two_sum_fast(nums, target)
        
        # Если перебор нашел пару, проверяем, что она реально дает target
        if res_brute is not None:
            i, j = res_brute
            assert nums[i] + nums[j] == target, f"two_sum_brute наврал: {nums[i]} + {nums[j]} != {target}"
            
        if res_fast is not None:
            i, j = res_fast
            assert nums[i] + nums[j] == target, f"two_sum_fast наврал: {nums[i]} + {nums[j]} != {target}"
            
        # Быстрый и медленный должны согласиться: либо оба нашли, либо оба нет
        assert (res_brute is None) == (res_fast is None), f"Расхождение: brute={res_brute}, fast={res_fast} на {nums}"


if __name__ == "__main__":
    random.seed(42) # Фиксируем seed для повторяемости
    
    # Проверяем все три сортировки
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn, trials=100)
        
    check_search()
    check_two_sum(trials=100)
    
    print("OK: все проверки пройдены успешно!")
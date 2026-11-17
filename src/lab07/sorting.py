def bubble_sort(nums: list) -> list:
    """Новый список, отсортированный по возрастанию. Исходный не меняется.

    bubble_sort([3, 1, 2]) -> [1, 2, 3]
    bubble_sort([2, 2, 1]) -> [1, 2, 2]
    bubble_sort([]) -> []
    """
    arr = list(nums) # Создаем копию, чтобы не менять исходный
    n = len(arr)
    
    for i in range(n):
        swapped = False # Флаг для раннего выхода (звездочка в задании)
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break # Если обменов не было, массив уже отсортирован
            
    return arr


def insertion_sort(nums: list) -> list:
    """Тот же контракт, что у bubble_sort."""
    arr = list(nums)
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Сдвигаем элементы, которые больше key, вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
        
    return arr


def selection_sort(nums: list) -> list:
    """Тот же контракт, что у bubble_sort."""
    arr = list(nums)
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        # Ищем минимум в оставшейся части
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Меняем местами текущий и найденный минимум
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

def merge_sort(nums: list) -> list:
    """Итеративная (снизу вверх) сортировка слиянием."""
    arr = list(nums)
    n = len(arr)
    width = 1
    
    # Пока размер сливаемых кусков меньше длины массива
    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            
            # Слияние двух отсортированных кусков
            merged = []
            l_idx, r_idx = 0, 0
            while l_idx < len(left) and r_idx < len(right):
                if left[l_idx] <= right[r_idx]:
                    merged.append(left[l_idx])
                    l_idx += 1
                else:
                    merged.append(right[r_idx])
                    r_idx += 1
            
            # Добавляем остатки
            merged.extend(left[l_idx:])
            merged.extend(right[r_idx:])
            
            # Вставляем обратно в массив
            arr[i:i + len(merged)] = merged
            
        width *= 2
        
    return arr


def counting_sort(nums: list, lo: int, hi: int) -> list:
    """Сортировка подсчетом для целых чисел в диапазоне [lo, hi]."""
    if not nums:
        return []
        
    # Создаем массив для подсчета (размер = диапазон значений)
    count_size = hi - lo + 1
    counts = [0] * count_size
    
    # Считаем количество каждого числа
    for x in nums:
        counts[x - lo] += 1
        
    # Восстанавливаем отсортированный массив
    result = []
    for i in range(count_size):
        result.extend([i + lo] * counts[i])
        
    return result
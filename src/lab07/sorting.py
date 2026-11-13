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
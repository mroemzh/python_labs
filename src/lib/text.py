import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Нормализует текст: регистр, ё→е, схлопывание пробелов.

    Args:
        text: исходная строка.
        casefold: если True — использовать str.casefold(), иначе str.lower().
        yo2e: если True — заменить ё/Ё на е/Е.

    Returns:
        Нормализованная строка.
    """
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    return " ".join(text.split())


def tokenize(text: str) -> list[str]:
    """Разбивает текст на слова по шаблону \\w+(?:-\\w+)*.

    Args:
        text: нормализованный текст.

    Returns:
        Список токенов.
    """
    return re.findall(r"\w+(?:-\w+)*", text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Считает частоты токенов.

    Args:
        tokens: список слов.

    Returns:
        Словарь слово → количество вхождений.
    """
    freq: dict[str, int] = {}
    for tok in tokens:
        freq[tok] = freq.get(tok, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Возвращает топ-N слов по убыванию частоты.

    При равенстве частот сортирует по алфавиту.

    Args:
        freq: словарь слово → количество.
        n: сколько слов вернуть.

    Returns:
        Список кортежей (слово, количество).
    """
    items = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return items[:n]
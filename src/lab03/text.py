import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace("ё", "е")

    return " ".join(text.split())


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+(?:-\w+)*", text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq: dict[str, int] = {}
    for tok in tokens:
        freq[tok] = freq.get(tok, 0) + 1
    return freq


def top_n(freq: dict[str, int], n) -> list[tuple[str, int]]:
    items = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return items[:n]


raw = input()
norm = normalize(raw)
print(norm)

tokens = tokenize(norm)
print(tokens)

n = 5
if tokens and tokens[-1].isdigit():
    n = int(tokens[-1])
    tokens = tokens[:-1]

freq = count_freq(tokens)
print(freq)

print(top_n(freq,n))
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.text import normalize, tokenize, count_freq, top_n


raw = sys.stdin.read()

norm = normalize(raw)
tokens = tokenize(norm)
freq = count_freq(tokens)

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")
for word, cnt in top_n(freq, 5):
    print(f"{word}:{cnt}")
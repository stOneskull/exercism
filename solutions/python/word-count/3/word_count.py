import re
from collections import Counter


def count_words(phrase):
    words_with_quotes = re.findall(
        r"[a-z0-9]+(?:'[a-z0-9]+)*", phrase.lower()
        )
    words = [word.strip("'") for word in words_with_quotes]
    return Counter(words)

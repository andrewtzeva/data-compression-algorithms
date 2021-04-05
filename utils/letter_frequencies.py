from collections import Counter
import re

text = open('example-texts/mobydick.txt')
text = text.read().replace('\n', ' ').upper()
text = ''.join(e for e in text if e.isalpha() or e.isspace())
final_text = re.sub(' +', ' ', text)


def find_freqs():
    frequencies = Counter(final_text)
    for letter, value in frequencies.items():
        frequencies[letter] = 100 * value / len(final_text)
    return frequencies


freqs = find_freqs()

example = open('example-texts/oliver_twist.txt')
example = example.read().replace('\n', ' ').lower()
example = ''.join(e for e in example if e.isalpha() or e.isspace())
final_example = re.sub(' +', ' ', example)
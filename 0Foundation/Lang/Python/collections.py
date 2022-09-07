from collections import Counter

a = ["abc", "abc", "def", "abc"]
counter_dict = Counter(a)

print(counter_dict.get("abcd", 0))
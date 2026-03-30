# Arrays & Strings Notes

## Core built-in functions

| Function | What it does | Example |
|----------|--------------|---------|
| `len(obj)` | Length of string/list/dict/set/tuple | `if len(nums) == 0:` |
| `enumerate(iterable, start=0)` | Index + value pairs | `for i, num in enumerate(nums):` |
| `all(iterable)` | True if all items are truthy | `if all(v == 0 for v in freq.values()):` |
| `any(iterable)` | True if any item is truthy | `if any(c not in freq for c in t):` |
| `zip(*iterables)` | Parallel iteration | `for a, b in zip(nums1, nums2):` |
| `sorted(iterable, key=None, reverse=False)` | Return sorted list | `sorted(s) == sorted(t)` |
| `reversed(seq)` | Reverse iterator | `reversed(s)` |
| `range(start, stop, step=1)` | Number sequence | `for i in range(1, len(nums)):` |
| `sum(iterable, start=0)` | Sum of numbers | `total = sum(nums)` |
| `max(iterable, key=None)` / `min(...)` | Max/min value | `max(nums, key=lambda x: x[1])` |
| `map(func, iterable)` | Apply function to each item | `list(map(int, digits))` |
| `filter(func, iterable)` | Keep items where func returns True | `list(filter(lambda x: x > 0, nums))` |
| `abs(x)` | Absolute value | `abs(i - j)` |
| `ord(c)` / `chr(i)` | Char ↔ ASCII code | `ord('a') == 97` |
| `set(iterable)` | Unique values and membership checks | `if num in seen:` |
| `lower()` | changes the whole string to lower case | `words.lower()` |
| `upper()` | changes the whole string to lower case | `words.upper()` |
| `isalnum()` | Checks if character is alphanumeric | `x.isalnum()` |
| `set(iterable)` | Removes leading/trailing whitespace | `words.strip()` |
| `join()` | used to join string and lists | `x = "".joined(list[],dict{})` |




## Quick reminders

- When a problem mentions "unique" or "duplicates," think `set` first.
- When it asks for a pair or sum, think `dict`/hash map for complements.
- When it asks for reversal, think slicing `[::-1]`.
- When it asks if two strings are permutations/anagrams, compare counts or sorted results.

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
| `lower()` | Changes the whole string to lower case | `words.lower()` |
| `upper()` | Changes the whole string to upper case | `words.upper()` |
| `isalnum()` | Checks if character is alphanumeric | `x.isalnum()` |
| `strip()` | Removes leading/trailing whitespace | `words.strip()` |
| `join(seq)` | Join iterable into a string | `x = "".join(['a','b'])` |
| `str(x)` | Convert value to string | `s = str(123)` |
| `int(x)` | Convert value to integer | `n = int('42')` |
| `float(x)` | Convert value to float | `f = float('3.14')` |
| `list(x)` | Convert iterable to list | `lst = list('abc')` |
| `tuple(x)` | Convert iterable to tuple | `t = tuple([1,2])` |
| `bool(x)` | Convert value to boolean | `flag = bool('')` |
| `type(obj)` | Inspect object type | `type(nums) is list` |
| `isinstance(obj, type)` | Check object type | `if isinstance(s, str):` |
| `str.isdigit()` | Check if all chars are digits | `if s.isdigit():` |
| `str.isalpha()` | Check if all chars are letters | `if name.isalpha():` |
| `str.isalnum()` | Check if all chars are alphanumeric | `if token.isalnum():` |
| `str.isspace()` | Check if all chars are whitespace | `if c.isspace():` |

adding two int arrays `nums + nums` will return the two arrays combined


## Quick reminders

- When a problem mentions "unique" or "duplicates," think `set` first.
- When it asks for a pair or sum, think `dict`/hash map for complements.
- When it asks for reversal, think slicing `[::-1]`.
- When it asks if two strings are permutations/anagrams, compare counts or sorted results.

## Data Structures in Python

Python provides several built-in data structures, each designed for specific use cases:

- **Lists**: Mutable, ordered sequences that can hold elements of any type. Support indexing, slicing, and in-place modifications.
- **Sets**: Mutable, unordered collections of unique elements. Excellent for membership testing and eliminating duplicates.
- **Dictionaries**: Mutable, unordered mappings of key-value pairs. Provide fast lookups by key.
- **Tuples**: Immutable, ordered sequences. Similar to lists but cannot be modified after creation.
- **Strings**: Immutable sequences of characters with specialized text manipulation methods.

### Lists

Lists are versatile containers for ordered data.

- `append(item)`: Add item to the end
  - `nums.append(5)`
- `insert(index, item)`: Insert item at specific index
  - `nums.insert(0, 1)`
- `pop(index=-1)`: Remove and return item at index (default last)
  - `removed = nums.pop()`
- `remove(item)`: Remove first occurrence of item
  - `nums.remove(3)`
- `sort(key=None, reverse=False)`: Sort list in place
  - `nums.sort()`
- `reverse()`: Reverse list in place
  - `nums.reverse()`
- `extend(iterable)`: Add all items from iterable
  - `nums.extend([4, 5, 6])`
- Indexing and slicing: `nums[0]`, `nums[-1]`, `nums[1:3]`
- Iteration: `for num in nums:`, `for i, num in enumerate(nums):`

### Sets

Sets store unique elements and provide fast membership tests.

- `add(item)`: Add item to set
  - `s.add(1)`
- `remove(item)`: Remove item (raises KeyError if not present)
  - `s.remove(1)`
- `discard(item)`: Remove item (no error if not present)
  - `s.discard(1)`
- `pop()`: Remove and return arbitrary item
  - `item = s.pop()`
- `clear()`: Remove all items
  - `s.clear()`
- Set operations: `union()`, `intersection()`, `difference()`, `symmetric_difference()`
  - `new_set = s1.union(s2)`
- Membership: `if x in s:`
- Iteration: `for item in s:`

### Dictionaries

Dictionaries map keys to values for efficient lookups.

- `d[key] = value`: Set or update value for key
  - `d['name'] = 'Alice'`
- `get(key, default=None)`: Get value for key, return default if not found
  - `val = d.get('age', 0)`
- `pop(key, default=None)`: Remove and return value for key
  - `val = d.pop('name')`
- `popitem()`: Remove and return arbitrary key-value pair
  - `k, v = d.popitem()`
- `keys()`: Return view of keys
  - `for k in d.keys():`
- `values()`: Return view of values
  - `for v in d.values():`
- `items()`: Return view of key-value pairs
  - `for k, v in d.items():`
- `update(other)`: Update with key-value pairs from other dict/iterable
  - `d1.update(d2)`
- Membership: `if key in d:`
- Iteration: `for k in d:`, `for k, v in d.items():`

### Tuples

Tuples are immutable sequences, often used for fixed collections of items.

- `index(item)`: Find index of first occurrence
  - `idx = t.index(5)`
- `count(item)`: Count occurrences of item
  - `count = t.count(3)`
- Indexing and slicing: `t[0]`, `t[-1]`, `t[1:3]`
- Iteration: `for item in t:`, `for i, item in enumerate(t):`
- Unpacking: `a, b, c = t`

### Strings

Strings are immutable sequences of characters with text-specific operations.

- `upper()` / `lower()`: Change case
  - `s.upper()`, `s.lower()`
- `strip(chars=None)`: Remove leading/trailing characters (default whitespace)
  - `s.strip()`
- `split(sep=None, maxsplit=-1)`: Split into list
  - `words = s.split()`
- `join(iterable)`: Join iterable with string as separator
  - `joined = " ".join(words)`
- `replace(old, new, count=-1)`: Replace substrings
  - `new_s = s.replace("old", "new")`
- `find(sub, start=0, end=-1)`: Find substring index
  - `idx = s.find("word")`
- `startswith(prefix)` / `endswith(suffix)`: Check prefixes/suffixes
  - `if s.startswith("Hello"):`
- `isalpha()` / `isdigit()` / `isalnum()` / `isspace()`: Character type checks
  - `if s.isdigit():`
- Indexing and slicing: `s[0]`, `s[-1]`, `s[1:3]`, `s[::-1]` (reverse)
- Iteration: `for c in s:`, `for i, c in enumerate(s):`

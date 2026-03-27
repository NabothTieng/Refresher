# Python Data Structures + CRUD Operations (DSA Style) 🐍

A clean, comprehensive guide to **Create, Read, Update, Delete (CRUD)** operations on all major Python data structures — optimized for **Data Structures and Algorithms (DSA)** interviews (LeetCode, Codeforces, HackerRank, etc.).

Perfect for quick revision, interview prep, and as a reference cheat sheet.

---

## ✨ Features

- Complete CRUD for every common Python data structure
- Time complexities included
- Real DSA use cases and idiomatic patterns
- Clean, professional GitHub-ready formatting
- Mini summary table for fast revision

---

## 📋 Table of Contents

- [1. List (`list`)](#1-list-list)
- [2. Set (`set`)](#2-set-set)
- [3. Dictionary / Hash Map (`dict`)](#3-dictionary--hash-map-dict)
- [4. Stack (using `list`)](#4-stack-using-list)
- [5. Queue (`collections.deque`)](#5-queue-collectionsdeque)
- [6. Deque (`collections.deque`)](#6-deque-collectionsdeque)
- [7. Heap / Priority Queue (`heapq`)](#7-heap--priority-queue-heapq)
- [8. String (`str`)](#8-string-str)
- [9. Tuple (`tuple`)](#9-tuple-tuple)
- [10. Linked List (Custom)](#10-linked-list-custom-class)
- [11. Nested Structures](#11-nested-structures)
- [12. Common CRUD Patterns in DSA](#12-common-crud-patterns-in-dsa)
- [13. Which Structure Is Most Idiomatic?](#13-which-structure-is-most-idiomatic)
- [14. Mini Summary (Fast Revision)](#14-mini-summary-fast-revision-sheet)
- [15. Best Interview Tips](#15-best-interview-tips)
- [16. Final Takeaway](#16-final-takeaway)

---

## 1. List (`list`)

Ordered, mutable, allows duplicates. The workhorse of Python.

### CRUD Operations

#### Create / Insert
```python
nums = []
nums.append(5)                    # O(1) amortized
nums.insert(0, 10)                # O(n)
nums.extend([7, 8, 9])            # O(k)
```

#### Read
```python
nums[2]                           # O(1)
5 in nums                         # O(n)
len(nums)
```

#### Update
```python
nums[1] = 99                      # O(1)
```

#### Delete
```python
nums.pop()                        # O(1) - last item
nums.pop(0)                       # O(n) - first item
nums.remove(5)                    # O(n) - first occurrence
del nums[2]                       # O(n)
nums.clear()
```

### When to Use
Arrays, dynamic lists, stacks, order matters.

### Time Complexity
- Access by index: **O(1)**
- Append: **O(1)** amortized
- Insert/Delete in middle: **O(n)**
- Search: **O(n)**

## 2. Set (`set`)

Unordered, unique elements, extremely fast lookups.

### CRUD Operations

#### Create / Insert
```python
seen = set()
seen.add(42)                      # O(1) avg
```

#### Read
```python
42 in seen                        # O(1) avg
len(seen)
```

#### Update
```python
seen.remove(42)                   # raises KeyError if missing
seen.discard(42)                  # safe (no error)
seen.add(99)                      # remove + add pattern
```

#### Delete
```python
seen.remove(10)
seen.discard(10)                  # preferred
seen.pop()                        # removes arbitrary element
seen.clear()
```

### When to Use
Deduplication, fast membership tests, visited nodes, graph traversal.

### Time Complexity
All operations **O(1)** average.

### DSA Example: Contains Duplicate
```python
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```
## 3. Dictionary / Hash Map (`dict`)

Key-value pairs. The most powerful built-in structure in Python.

### CRUD Operations

#### Create / Insert
```python
mp = {}
mp["key"] = "value"
mp.update({"a": 1, "b": 2})
```

#### Read
```python
mp["key"]                         # KeyError if missing
mp.get("key")                     # returns None
mp.get("key", 0)                  # with default
"key" in mp
len(mp)
```

#### Update
```python
mp["key"] = "new_value"
```

#### Delete
```python
del mp["key"]                     # KeyError if missing
mp.pop("key")                     # returns value, raises KeyError
mp.pop("key", None)               # safe
mp.clear()
```

### When to Use
Frequency counting, caching, mapping relationships, adjacency lists.

### Time Complexity
All operations **O(1)** average.

### DSA Example: Frequency Map
```python
count = {}
for num in nums:
    count[num] = count.get(num, 0) + 1
```
## 4. Stack (using `list`)

LIFO (Last In, First Out)

### CRUD Operations

```python
stack = []

# Push - O(1)
stack.append(val)

# Peek  - O(1)
stack[-1]

# Update top
stack[-1] = new_val

# Pop   - O(1)
stack.pop()
```

### Use Cases
Parentheses validation, backtracking, DFS, monotonic stack.
## 5. Queue (`collections.deque`)

FIFO (First In, First Out) — Always use `deque` for queues!

### CRUD Operations

```python
from collections import deque

q = deque()

# Enqueue right - O(1)
q.append(val)

# Front (peek)
q[0]

# Update front
q[0] = new_val

# Dequeue - O(1)
q.popleft()
```

⚠️ **Never use `list.pop(0)` → O(n)**

### Use Cases
BFS, sliding window, task scheduling.
## 6. Deque (`collections.deque`)

Double-ended queue — efficient operations on both ends.

### CRUD Operations

```python
from collections import deque

dq = deque()

# Append operations
dq.append(val)                    # right
dq.appendleft(val)                # left

# Read operations
dq[0]                             # front
dq[-1]                            # back

# Delete operations
dq.pop()                          # remove right
dq.popleft()                      # remove left
```

### Use Cases
Sliding window, monotonic queue, LRU cache.
## 7. Heap / Priority Queue (`heapq`)

Min-heap by default.

### CRUD Operations

```python
import heapq

heap = []

# Push - O(log n)
heapq.heappush(heap, val)

# Peek min - O(1)
heap[0]

# Pop - O(log n)
smallest = heapq.heappop(heap)
```

### Max Heap Workaround
```python
# Push negative to simulate max heap
heapq.heappush(heap, -val)

# Pop and negate back
max_val = -heapq.heappop(heap)
```

### Useful Functions
```python
heapq.heapify(list)               # Build heap in-place - O(n)
heapq.nlargest(k, nums)           # Top k largest
heapq.nsmallest(k, nums)          # Top k smallest
```

### Use Cases
Top K elements, merge K sorted lists, Dijkstra, scheduling.
## 8. String (`str`)

Immutable sequence.

### CRUD Operations

```python
s = "hello"

# Create (concatenation creates new string) - O(n)
s = s + "!"

# Update/Delete (slicing creates new string)
s = s[:i] + "x" + s[i+1:]
```

### Use Cases
Two pointers, sliding window, palindrome problems.
## 9. Tuple (`tuple`)

Immutable list. Hashable → can be used in sets and dict keys.

### CRUD Operations

```python
pair = (1, 2)

# Common use in grid problems - O(1) to add to set
visited.add((row, col))
```

### Use Cases
Grid coordinates, hashable keys, unpacking values.
## 10. Linked List (Custom Class)

### Class Definition

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### Common Operations
- Head insertion
- Delete next node
- Reverse
- Merge
- Fast/slow pointers
## 11. Nested Structures

Very common in interviews.

### Graph - Adjacency List
```python
graph = {}
graph.setdefault(u, []).append(v)
```

### Anagram Groups
```python
groups = {}
for word in words:
    key = "".join(sorted(word))
    groups.setdefault(key, []).append(word)
```
## 12. Common CRUD Patterns in DSA

- **Frequency Counting** → `dict`
- **Visited Tracking** → `set`
- **Adjacency List** → `dict[list]`
- **Grouping/Anagrams** → `dict[list]`


## 13. Which Structure Is Most Idiomatic?

| Need                          | Best Structure     |
|-------------------------------|--------------------|
| Existence / Deduplication     | `set`              |
| Counts / Frequency            | `dict`             |
| Ordered + Duplicates          | `list`             |
| LIFO (Stack)                  | `list`             |
| FIFO (Queue)                  | `deque`            |
| Both ends fast                | `deque`            |
| Priority / Top-K              | `heapq`            |
| Key → Value mapping           | `dict`             |
| Pointer manipulation          | Linked List        |

---

## 14. Mini Summary (Fast Revision Sheet)

| Structure   | Insert                          | Read               | Update                | Delete                     | Key Complexity                  |
|-------------|---------------------------------|--------------------|-----------------------|----------------------------|---------------------------------|
| **list**    | `append()`, `insert()`          | `lst[i]`           | `lst[i] = x`          | `pop()`, `remove()`        | Access **O(1)**, Mid **O(n)**   |
| **set**     | `add()`                         | `x in s`           | remove + add          | `remove()`, `discard()`    | **O(1)** avg                    |
| **dict**    | `d[k] = v`                      | `d[k]`, `d.get()`  | `d[k] = new`          | `del d[k]`, `pop()`        | **O(1)** avg                    |
| **Stack**   | `append()`                      | `[-1]`             | `[-1] = x`            | `pop()`                    | **O(1)**                        |
| **Queue**   | `append()`                      | `[0]`              | `[0] = x`             | `popleft()`                | **O(1)**                        |
| **Deque**   | `append()`, `appendleft()`      | `[0]`, `[-1]`      | `[0]=x`, `[-1]=x`     | `pop()`, `popleft()`       | **O(1)**                        |
| **Heap**    | `heappush()`                    | `heap[0]`          | Rebuild / lazy        | `heappop()`                | **O(log n)**                    |
| **String**  | Slicing + concat                | `[i]`              | Slicing               | Slicing                    | **O(n)**                        |

## 15. Best Interview Tips

When approaching any DSA problem, ask yourself:

- Do I need order? → `list` or `deque`
- Do I need uniqueness? → `set`
- Do I need key-value? → `dict`
- Do I need priority/min/max? → `heapq`
- Do I need fast removal from front? → `deque`
- Do I need pointer manipulation? → Linked List

## 16. Final Takeaway

Mastering CRUD operations on Python's data structures is one of the fastest ways to improve your DSA speed and code quality.

Use the right tool for the job and your solutions will be cleaner, faster, and more Pythonic.

---

**Made with ❤️ for Python DSA learners**

Feel free to star ⭐ this repo if it helped you!
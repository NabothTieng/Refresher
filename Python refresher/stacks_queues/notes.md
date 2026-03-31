# 📝 Revision Notes: Stack Data Structure

## 1. What is a Stack?

| Property | Description |
|----------|-------------|
| **Type** | Linear data structure |
| **Principle** | LIFO (Last-In-First-Out) |
| **Analogy** | Pile of plates, browser history, undo button |
| **Use case** | Track "most recent" or "nested" items |

```
  ┌─────┐  ← Top (access/remove here)
  │  C  │
  ├─────┤
  │  B  │
  ├─────┤
  │  A  │  ← Bottom
  └─────┘
```

---

## 2. Core operations (Python list as stack)

| Operation | Syntax | Time complexity | Purpose |
|-----------|--------|-----------------|---------|
| **Push** | `stack.append(item)` | O(1) | Add to top |
| **Pop** | `stack.pop()` | O(1) | Remove and return top |
| **Peek** | `stack[-1]` | O(1) | View top without removing |
| **Empty check** | `if not stack:` or `len(stack) == 0` | O(1) | Check if empty |
| **Size** | `len(stack)` | O(1) | Get number of elements |

> Important: always check `if stack:` before `pop()` or `stack[-1]` to avoid `IndexError`.

---

## 3. When to use a stack (pattern recognition)

| Signal in problem | Likely stack pattern |
|-------------------|----------------------|
| "Matching pairs" (brackets, tags) | ✅ Match opening/closing |
| "Nested structure" | ✅ Track depth/levels |
| "Last seen" or "most recent" | ✅ LIFO access |
| "Undo/Redo" functionality | ✅ Reverse order |
| "Reverse" something | ✅ Natural reversal |
| "Next greater/smaller element" | ✅ Monotonic stack |
| "Valid sequence" | ✅ Validate order |
| Depth-first traversal | ✅ DFS (recursion = implicit stack) |

---

## 4. Common stack problem types

### A. Matching/balance problems
- Valid Parentheses
- Valid Bracket Sequence
- HTML Tag Validation

### B. Next greater/smaller element
- Next Greater Element I & II
- Daily Temperatures
- Stock Span Problem

### C. Expression evaluation
- Evaluate Reverse Polish Notation
- Basic Calculator
- Min Stack

### D. Monotonic stack
- Largest Rectangle in Histogram
- Trapping Rain Water
- Sum of Subarray Minimums

### E. Path/history tracking
- Simplify Path (Unix file paths)
- Backspace String Compare
- Remove K Digits

---

## 5. Stack implementation templates

### Basic template
```python
def stack_problem(arr):
    stack = []

    for item in arr:
        # Process current item
        while stack and <condition>:
            stack.pop()

        stack.append(item)

    return result
```

### Monotonic increasing stack
```python
stack = []
for num in nums:
    while stack and stack[-1] > num:
        stack.pop()
    stack.append(num)
```

### Monotonic decreasing stack
```python
stack = []
for num in nums:
    while stack and stack[-1] < num:
        stack.pop()
    stack.append(num)
```

---

## 6. Python stack tips

| Tip | Code example |
|-----|--------------|
| Safe pop | `if stack: val = stack.pop()` |
| Safe peek | `if stack: top = stack[-1]` |
| Check empty | `if not stack:` or `if len(stack) == 0` |
| Clear stack | `stack.clear()` or `stack = []` |
| Copy stack | `new_stack = stack.copy()` |

### Using `collections.deque` for large stacks
```python
from collections import deque
stack = deque()
stack.append(item)   # Push
stack.pop()          # Pop
```
✅ More efficient for very large stacks (O(1) guaranteed)

---

## 7. Common mistakes

| Mistake | Issue | Fix |
|---------|-------|-----|
| `stack.pop` without `()` | Method reference, not execution | `stack.pop()` |
| No empty check before pop | `IndexError` | `if stack and ...` |
| Wrong end access | `stack[0]` is bottom, not top | Use `stack[-1]` |
| Forgetting final state | Stack may have leftovers | Check `return not stack` |
| Using stack when queue needed | FIFO vs LIFO confusion | Identify order requirement |

---

## 8. Complexity summary

| Operation | Time | Space |
|-----------|------|-------|
| Push | O(1) | O(1) |
| Pop | O(1) | O(1) |
| Peek | O(1) | O(1) |
| Search | O(n) | O(1) |
| **Overall problem** | O(n) | O(n) |

---

## 9. Problem-solving checklist

Before coding, ask:
1. ❓ Do I need LIFO order?
2. ❓ Am I matching pairs or validating sequence?
3. ❓ Do I need to track "most recent" element?
4. ❓ Should I use monotonic property?
5. ❓ What's stored in the stack — indices, values, or both?
6. ❓ When do I push? When do I pop?
7. ❓ What's the final stack state — empty or processed?

---

## 10. Practice problems by difficulty

| Easy | Medium | Hard |
|------|--------|------|
| Valid Parentheses | Evaluate RPN | Largest Rectangle in Histogram |
| Min Stack | Decode String | Trapping Rain Water |
| Implement Stack | Next Greater Element | Maximal Rectangle |
| Backspace Compare | Build Skyline | Remove K Digits |

---

**💡 Pro Tip:** When stuck, trace through an example with a **visual stack diagram**—draw what gets pushed/popped at each step!

---

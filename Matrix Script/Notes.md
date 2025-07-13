## Code
```
#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
columnwise = ''.join([matrix[i][j] for j in range(m) for i in range(n)])
pattern = r"(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])"
columnwise = re.sub(pattern," ",columnwise)
print(columnwise)


```
## Explanation
`columnwise = ''.join([matrix[i][j] for j in range(m) for i in range(n)])`
- This just reads the matrix columnwise and joins them without any space.
  `pattern = r"(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])"`
- `(?<=[a-zA-Z0-9])` checks for previous alphanumeric values
- `[^a-zA-Z0-9]+` checks for non-alphanumeric values occurs atleast once
- `(?=[a-zA-Z0-9])` checks for alphanumeric values ahead

  I asked ChatGPT for some extra information. Here it goes:



| Method                        | Description                                                          | Example                     | Output            |
| ----------------------------- | -------------------------------------------------------------------- | --------------------------- | ----------------- |
| `s.strip()`                   | Removes whitespace from both ends                                    | `"  hello \n".strip()`      | `"hello"`         |
| `s.rstrip()`                  | Removes whitespace from the right (end)                              | `"hello   \n".rstrip()`     | `"hello"`         |
| `s.lstrip()`                  | Removes whitespace from the left (start)                             | `"   hello".lstrip()`       | `"hello"`         |
| `s.split()`                   | Splits a string into a list (default: on whitespace)                 | `"a b c".split()`           | `['a', 'b', 'c']` |
| `s.split(',')`                | Splits a string by a given delimiter                                 | `"a,b,c".split(',')`        | `['a', 'b', 'c']` |
| `' '.join(list)`              | Joins a list of strings into one string, with separator `' '`        | `' '.join(['a', 'b', 'c'])` | `"a b c"`         |
| `s.replace(old, new)`         | Replaces all occurrences of `old` with `new`                         | `"a-b-c".replace('-', ' ')` | `"a b c"`         |
| `s.lower()` / `s.upper()`     | Converts the string to lowercase or uppercase                        | `"Hello".lower()`           | `"hello"`         |
| `s.isdigit()` / `s.isalpha()` | Checks if string contains only digits / only letters                 | `"123".isdigit()`           | `True`            |
| `s.isalnum()`                 | Checks if the string is alphanumeric (letters or digits, no symbols) | `"abc123".isalnum()`        | `True`            |
| `s.startswith('a')`           | Checks if the string starts with `'a'`                               | `"abc".startswith('a')`     | `True`            |
| `s.endswith('z')`             | Checks if the string ends with `'z'`                                 | `"xyz".endswith('z')`       | `True`            |
| `s.find('x')`                 | Returns index of first occurrence of `'x'`, or -1 if not found       | `"hello".find('e')`         | `1`               |
| `s.count('a')`                | Counts occurrences of `'a'` in the string                            | `"banana".count('a')`       | `3`               |



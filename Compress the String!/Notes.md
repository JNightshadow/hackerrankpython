## Understanding groupby() in python

I've been a .NET developer and in C# groupby() is very different. 
In python, using `groupby()` will result in consecutive elements in the list. Unlike in C# it would groupby the same elements.

Inorder to group them by the same element values, we use `defaultdict` and `Counter`.
Feeling intimidated already!

## Using `defaultdict`
```
from collections import defaultdict

s = "1222311"
groups = defaultdict(list)

for char in s:
    groups[char].append(char)

for k, g in groups.items():
    print(f"{k}: {g}")
```
Output:

```
1: ['1', '1', '1']
2: ['2', '2', '2']
3: ['3']
```

## Using `Counter`
```
from collections import Counter

s = "1222311"
counts = Counter(s)

print(counts)
```
Output:

`Counter({'2': 3, '1': 3, '3': 1})`

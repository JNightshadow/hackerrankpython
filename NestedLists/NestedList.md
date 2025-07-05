# Some examples

### Find the first match where second element == target_value, and get the first element
```
records = [
    ['a', 10],
    ['b', 20],
    ['c', 30],
    ['d', 20]
]

target_value = 20
```first_match = next((record[0] for record in records if record[1] == target_value), None)

print([first_match] if first_match is not None else [])

```
### Printing lists without the [ ]:
```
names = ['apple', 'banana', 'cherry']
print(' '.join(names))

nums = [10, 20, 30]
print(' '.join(str(x) for x in nums))

print(*nums)
```
### Printing elements of list with newline without a for loop:
```
items = ['apple', 'banana', 'cherry']
print(*items, sep='\n')

print('\n'.join(items))

nums = [10, 20, 30]
print('\n'.join(map(str, nums)))

```

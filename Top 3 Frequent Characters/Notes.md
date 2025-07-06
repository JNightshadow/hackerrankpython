```
def myfunct(e):
     return -e[1],e[0]
if __name__ == '__main__':
    s = input()
    counted =[[i,s.count(i) ]for i in set(s)]
    counted.sort(key = myfunct)
    print('\n'.join(map(lambda x: f"{x[0]} {x[1]}",counted[:3])))

```
## Explanation
` counted =[[i,s.count(i) ]for i in set(s)]`

- set(s) would give the unique elements.
- `i,s.count(i)` would return a list of each character with their count and store them as a list

`counted.sort(key = myfunct)` would sort based on the key which is:
```
def myfunct(e):
     return -e[1],e[0]
```
- `-e[1]` sorts the elements in reverse order of their frequencies
- `e[0]` would sort based on the character since in the problem they have mentioned to sort characters with equal frequencies in the alphabetical order.

` print('\n'.join(map(lambda x: f"{x[0]} {x[1]}",counted[:3])))`

- This prevents printing the square brackets [] and commas (,) which appears on printing the list as it is.
- `lambda x: f"{x[0]} {x[1]}"` would return for example `a 3` to x
- Then using `'\n'.join( ,listname)` we are concatenating each element line by line

```
from itertools import permutations
if __name__ == "__main__":
    S,k = input().split()
    p = list(permutations(S,int(k)))
    p.sort()
    print('\n'.join(''.join(j for j in i) for i in p))
```
The brackets really matter.. Please be careful while using these list comprehensions in one line. I kept getting error that I was trying to print the generator expression when I used this:
 print('\n'.join(''.join(j for j in i) $${\color{red})}$$ for i in p)

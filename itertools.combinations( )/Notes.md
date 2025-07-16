```
from itertools import combinations
if __name__ == "__main__":
    S,k = input().split()
    for count in range(1,int(k)+1):
        print('\n'.join(''.join(str(j) for j in i) for i in (combinations(sorted(S),count))))
```
I'm trying to print everything in one line. Hope it's not very confusing!
In order to make the combinations to be printed in an alphabetical order, all I had to do was sort the input!
I am getting the hang of these list comprehensions.. I think 😅
- So what I'm doing here is sorting the combinations for r =1,2,.. k (Hence I've used `range(1,int(k)+1)`)
- Whatever's in the print line may seem complicated but it's just:

```
    k = int(k)
    S = sorted(S)
    for count in range(1,k+1):
        for i in combinations(S,count):
            print(''.join(i))
```
... which I admit would be easier to understand. But I just have a problem of complicating things.

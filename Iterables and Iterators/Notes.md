```
from itertools import combinations
if __name__ == '__main__':
    n = int(input())
    letters = input().split()
    k = int(input())
    tuples = list(combinations(letters,k))
    a_count = sum([1 for x in tuples if "a" in x])
    print(float(a_count/len(tuples)))
```

itertools allow us to use tools like combinations, permutations, etc. Link have been given in the referencers.
 `letters = input().split()`
- This splits the input by space.
- Combinations would create combinations of the input without repetitions.

  ` a_count = sum([1 for x in tuples if "a" in x])`
-  This loops through the combinations stored in `tuple`. The number of values in each entry can depend upon k. If k is given as 3 that means each combination can have 3 elements. That's why we are using `"a" in x` since while looping through `tuples` we would get a k-element entry.
-  I initially made the mistake of `sum([1 for x in tuples if x[0] == 'a' or x[1] == 'a')` this would only check for first two elements and depending on k, the length of x would vary.<br>
<ins>Counting 'a' using lambda expression:</ins>
`a_count = len(list(filter(lambda x: 'a' in x, tuples)))`
- In this case lambda function would return the values for which `'a' in x` is true and would filter those values from tuples.
- Since filter returns iterator we have to make it into a list() type object inorder to count it.
- What is an iterator? It produces the values but does not store them yet. So if we tried to count them it would return some error:
  `<itertools.combinations object at 0x...>` - Is the error I encountered when I tried to store the combinations without converting it into a list.
## References

[itertools](https://docs.python.org/3/library/itertools.html)

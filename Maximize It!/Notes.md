# Code
```
from itertools import product
if __name__ == "__main__":
    k,m = map(int,input().split())
    klist = []
    for _ in range(k):
        elements = list(map(int,input().split()))
        klist.append(elements[1:])
    cartesian_product = list(product(*klist))
    maximum = float('-inf')
    for x in cartesian_product:
        total = (sum(i**2 for i in x))%m
        maximum = max(maximum,total)
    print(maximum)
```
# Explanation
The input is expected in the following format:
```
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10
```
- `input().split` is used two times. 
  - `map()` is used first time to convert it into int and store in two seperate variables k and m
  - In the second case we are converting multiple space seperated inputs and converting them into list as map only gives an iterator.
- Since we do not need the first element (as we've been given, it is the size of the array in each line) we store the rest in `klist`
- We are using `product` operation from the library `itertools` inorder to obtain the Cartesian Product.
- We use * so that every element within sub array is also used to make the product.
- We loop through the Cartesian product which now has all possible combinations of the list of numbers.
- We need to find one element each from the set of arrays we are giving as input such that it maximises the sum of squares of each element modulus of m.
  - This is done in the second loop.

## References
[itertools](https://docs.python.org/3/library/itertools.html#itertools.combinations)

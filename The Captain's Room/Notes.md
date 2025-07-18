```
from collections import Counter
if __name__ == "__main__":
    input()
    room_allocations = input().split()
    print(next(key for key,value in Counter(room_allocations).items()
                if value == 1))
```
Counter gives us a key,value pair of element and its count. For the given problem, we just need to print the key whose count is 1.
                if value == 1))
> [!TIP]
> `next()` will print the first value that matches the condition while traversing through the list.

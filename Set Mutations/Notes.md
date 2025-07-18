```
if __name__ == "__main__":
    input()
    A = set(input().split())
    N = int(input())
    for i in range(N):
        operation, length = input().split()
        B = input().split()
        getattr(A,operation)(set(B))
    print(sum(map(int,A)))
```
This code is pretty explanatory but I wanted to note down the mistake I made.
- If I don't convert A into set before doing all the operations through `getattr()`, the operations don't make any changes to A!
- Hence it is necessary to modify `A` as a set in the beginning itself inorder to reflect the changes after all the consecutive operations done.

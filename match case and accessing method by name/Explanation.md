In python we do not have switch case! Instead it's called match case though I do not know why they couldn't keep the same name.. 
I asked chatgpt for an efficient way instead of implementing the `match case` which seemed redundant and no different to the `if elif` statements.
So I was introduced to `getattr(object, 'attr_name')`

```
if __name__ == '__main__':
    N = int(input())
    array = []
    for _ in range(N):
        inputs = input().split()
        command,args= inputs[0], list(map(int,inputs[1:]))
        if command == 'print':
            print(array)
        else:
            getattr(array,command)(*args)
```
- Here, the first argument of getattr is the variable on which we have to do the operation
- `command` is a string which is the operation we need to perform.
-   For our problem the `command` contains the values `insert, append,` etc.
 `getattr(array, 'insert')(*[3,4)` is the same as `array.insert(3,4)`
-   `print()` cannot be passed as it is not a list method but a built-in function
Hence we reduced the number of statements using `getattr()`!

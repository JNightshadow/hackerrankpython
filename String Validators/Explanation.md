Here is solution for checking without using a lot of  `if-else ` statements:
```
if __name__ == '__main__':
    s = input()
    operations = ["isalnum","isalpha","isdigit","islower","isupper"]
    for i in operations:
        print(any(getattr(c,i)() for c in s))
```

`getattr(obj,operation_name)` lets you pass the operation name as a string and execute it.
> [!WARNING]
> The brackets after `getattr(obj,operation_name)()` is necessary for it to execute. It's the same as not using the function brackets to execute.
> <br> ❌ `getattr("hello","islower")` is the same as `"hello".islower`
> <br> ✔️ `getattr("hello","islower")()` is equivalent to `"hello".islower()`

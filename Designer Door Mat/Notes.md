```
if __name__ == "__main__":
    n, m = map(int, input().split())
    pattern = ".|."
    welcome = "WELCOME"

    for i in range(n):
        if i == n // 2:
            print(welcome.center(m, "-"))
        else:
            if i < n // 2:
                count = 2 * i + 1
            else:
                count = 2 * (n - i - 1) + 1
            line = pattern * count
            print(line.center(m, "-"))
```
    
- `print(welcome.center(m, "-"))` - Prints a string of width m. The contents of the variable `welcome` will placed at the center, with dashes filled.
- Up to middle of n, the number of patterns will be increasing, after that decreasing and mirroring the top portion of the pattern.
- `line` contains the middle patterns hence it is printed at the center with dashes filled on either sides.

# Enter your code here. Read input from STDIN. Print output to STDOUT
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
    

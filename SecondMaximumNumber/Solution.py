if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    first = float('-inf')
    runner = float('-inf')
    for i in arr:
        if(i>first):
            runner = first
            first = i
        elif(i<first and i>runner):
            runner = i
    print(runner)

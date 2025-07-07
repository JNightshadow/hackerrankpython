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

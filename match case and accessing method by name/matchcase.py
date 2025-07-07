N = int(input())
    array = []
    for _ in range(N):
        a = input().split()
        op = a[0]
        num = list(map(int, a[1:]))
        match (op):
            case 'insert':
                array.insert(num[0],num[1])
            case 'print':
                print(array)
            case 'remove':
                array.remove(num[0])
            case 'append':
                array.append(num[0])
            case 'sort':
                array.sort()
            case 'pop':
                array.pop()
            case 'reverse':
                array.reverse()

def merge_the_tools(string, k):
    list = []
    for i in range(0,len(string)-k+1,k):
        list.append(string[i:i+k])
    result =[]
    for i in list:
        group = []
        for c in i:
            if c not in group:
                group.append(c)
        result.append(''.join(group))
    print('\n'.join(result))
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

if __name__ == "__main__":
    A = set(map(int,input().split()))
    #print(A)
    flag = None
    for i in range(int(input())):
        subset = set(map(int,input().split()))
        #print(subset)
        if not subset.issubset(A):
            flag = False
            print(False)
            break
        else:
            flag = True
    if(flag):
        print(True)

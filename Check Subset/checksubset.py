if __name__ == "__main__":
    for _ in range(int(input())):
        input()
        A = set(map(int,input().split()))
        input()
        B = set(map(int,input().split()))
        print(A.issubset(B))

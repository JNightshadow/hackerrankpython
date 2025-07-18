if __name__ == "__main__":
    input()
    A = set(input().split())
    N = int(input())
    for i in range(N):
        operation, length = input().split()
        B = input().split()
        getattr(A,operation)(set(B))
    print(sum(map(int,A)))

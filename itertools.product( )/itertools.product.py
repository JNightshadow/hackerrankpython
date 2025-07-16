from itertools import product
if __name__ == "__main__":
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    print (' '.join(str(i) for i in (product(A,B))))

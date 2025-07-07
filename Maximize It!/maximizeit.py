# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
if __name__ == "__main__":
    k,m = map(int,input().split())
    klist = []
    for _ in range(k):
        elements = list(map(int,input().split()))
        klist.append(elements[1:])
    cartesian_product = list(product(*klist))
    maximum = float('-inf')
    for x in cartesian_product:
        total = (sum(i**2 for i in x))%m
        maximum = max(maximum,total)
    print(maximum)

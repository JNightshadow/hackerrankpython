from itertools import permutations
if __name__ == "__main__":
    S,k = input().split()
    p = list(permutations(S,int(k)))
    p.sort()
    print('\n'.join(''.join(j for j in i) for i in p))

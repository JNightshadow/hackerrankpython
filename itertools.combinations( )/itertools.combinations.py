from itertools import combinations
if __name__ == "__main__":
    S,k = input().split()
    for count in range(1,int(k)+1):
        print('\n'.join(''.join(str(j) for j in i) for i in (combinations(sorted(S),count))))

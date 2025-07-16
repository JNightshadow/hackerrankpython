from itertools import combinations_with_replacement
if __name__ == "__main__":
    S,k = input().split()
    S = sorted(S)
    k = int(k)
    print('\n'.join
                (''.join(str(j) for j in i)
                    for i in combinations_with_replacement(S,k)))

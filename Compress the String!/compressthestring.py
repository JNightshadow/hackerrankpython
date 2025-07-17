from itertools import groupby
if __name__ == "__main__":
    S = input()
    for k,g in groupby(S):
        print((len(list(g)),int(k)), end = ' ')

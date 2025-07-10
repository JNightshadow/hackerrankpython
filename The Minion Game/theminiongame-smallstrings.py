# O(n*n) as here im generating every single combination which is not ideal for longer strings
from itertools import starmap, combinations, repeat
from operator import getitem
def subslices(seq):
    slices = starmap(slice, combinations(range(len(seq) + 1), 2))
    return map(getitem, repeat(seq), slices)
def minion_game(string):
    words = list(subslices(string))
    vowels = ["A","E","I","O","U"]
    s = sum(1 for i in words if i[0] not in vowels)
    k = sum(1 for i in words if i[0] in vowels)
    if(s>k):
        print("Stuart",s)
    elif(k>s):
        print("Kevin",k)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

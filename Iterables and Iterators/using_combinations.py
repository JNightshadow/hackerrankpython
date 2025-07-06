from itertools import combinations
if __name__ == '__main__':
    n = int(input())
    letters = input().split()
    k = int(input())
    tuples = list(combinations(letters,k))
    a_count = sum([1 for x in tuples if "a" in x])
    print(float(a_count/len(tuples)))

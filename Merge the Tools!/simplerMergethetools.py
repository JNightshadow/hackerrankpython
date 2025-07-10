def merge_the_tools(string, k):
     for i in range(0, len(string), k):
        seen = set()
        chunk = string[i:i+k]
        print(''.join([c for c in chunk if not (c in seen or seen.add(c))]))
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

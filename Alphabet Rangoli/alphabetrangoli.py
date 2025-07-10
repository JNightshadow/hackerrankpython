def print_rangoli(size):
    width = 4*size-3
    for j in range(size):
        letters = [chr(i+96) for i in range(size,size-j-1,-1)]
        letters += letters[::-1][1:]
        print('-'.join(letters).center(width,'-'))
    for j in range(size-2,-1,-1):
        letters = [chr(i+96) for i in range(size,size-j-1,-1)]
        letters += letters[::-1][1:]
        print('-'.join(letters).center(width,'-'))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

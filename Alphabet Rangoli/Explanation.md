```
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
```

## Deriving `width = 4*size-3`

If size is 5 the pattern in the middle  using all the letters would be: `e-d-c-b-a-b-c-d-e`
- Just the letters alone would be of size: `size+size-1 = 2*size-1`
- Dashes would be inserted in the middle, hence number of dashes: `2*size-1-1 = 2*size-2`
- Adding both we get width as: `4*size-3`
We add 96 because small letters starts from 97(a) to 122(b) whereas capital letters are from 65(A) to 90(Z)
`letters[::-1]` reverses the list letters[].
While appending the reverse we dont need the letters hence `letters += letters[::-1][1:]`

I used the first loop for printing the first half, second for the rest. There might be simpler ways so please let me know! Feel free to contribute 😄

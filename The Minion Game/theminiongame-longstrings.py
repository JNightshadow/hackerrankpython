# without generating all strings.. this would be more optimal since we dont really need the strings. we just need the score :)
def minion_game(string):
    length = len(string)
    vowels = ["A","E","I","O","U"]
    s=0
    k=0
    for i in range(length):
        if string[i] in vowels:
            k += length-i
        else:
            s += length - i
    if(s>k):
        print("Stuart",s)
    elif(k>s):
        print("Kevin",k)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

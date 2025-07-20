from collections import Counter
if __name__ == "__main__":
    input()
    shoe_sizes = map(int,input().split())
    available_shoes = Counter(shoe_sizes)
    money_earned = 0
    for _ in range(int(input())):
        shoe_size, price = map(int,input().split())
        if shoe_size in available_shoes:
            if(available_shoes[shoe_size]>=1):
                available_shoes[shoe_size] -=1
                money_earned += price
    print(money_earned)

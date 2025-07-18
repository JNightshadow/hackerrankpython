from collections import Counter
if __name__ == "__main__":
    input()
    room_allocations = input().split()
    print(next(key for key,value in Counter(room_allocations).items()
                if value == 1))

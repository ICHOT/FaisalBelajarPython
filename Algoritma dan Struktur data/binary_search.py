def binary_seaarch(list, item):
    count = 0
    low = 0
    high = len(list)-1
    print("High", high)
    while low <= high:
        mid = (low+high) // 2
        guess = list[mid]
        count += 1
        print("Percobaan Ke: ", count)
        if guess == item:
            # return mid
            print("mid: ", mid)
        if guess > item:
            high = mid - 1
            print("High", high)
        else:
            low = mid + 1
            print("low", high)
    return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(binary_seaarch(my_list, 10))

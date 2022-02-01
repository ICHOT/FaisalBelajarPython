def binary_search(list, item):
    count = 0
    low = 0
    while low <= list:
        print("low: ", low, "high: ", list)
        mid = (low+list) // 2
        count += 1
        print("Percobaan Ke: ", count, " Hasil: ", mid)
        if mid == item:
            print("Tebakan Benar: ", mid)
            break
        if mid > item:
            list = mid - 1
            # print("High > ", list)
        else:
            low = mid + 1
            # print("low < ", list)
    return None


print(binary_search(1000, 500))

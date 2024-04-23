import random 
import time

# Slow method for searching elements in a l
def typ_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1
    
# Binary method for searching elements in a l
def bin_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return bin_search(l, target, low, midpoint-1)
    else:
        return bin_search(l, target, midpoint+1, high)
    
if __name__ == '__main__':
    # l = [1, 12, 33, 44, 56, 77, 98]
    # target = 12
    # print(typ_search(l,target))
    # print(bin_search(l,target))
    length = 10000

    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        typ_search(sorted_list, target)
    end = time.time()
    print("Typical search time: ", (end - start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        bin_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds")
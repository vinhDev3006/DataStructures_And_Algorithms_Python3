def sumRec(num_list: list[int]) -> int:
    if not num_list:
        return 0
    else:
        return num_list[0] + sumRec(num_list[1:])


print(sumRec([2, 4, 6]))
#12
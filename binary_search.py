def binary_search(r_list: list, req: int):
    lo = 0
    hi = len(r_list) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        print(r_list[lo: hi + 1])
        if r_list[mid] == req:
            return r_list[mid]
        elif r_list[mid] < req:
            lo = mid + 1
        else:
            hi = mid - 1

    return None


n_list = [-1, 0, 1, 3, 4, 4, 10]
print(binary_search(n_list, -1))

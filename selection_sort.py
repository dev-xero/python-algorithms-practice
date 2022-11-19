# The time complexity of this algorithm is O(n²)
def selection_sort(u_list: list):
    new_list = []
    # this function runs n times taking O(n) time
    for k in range(len(u_list)):
        # Return the smallest item in the array
        # This operation takes O(n) time
        i = 0
        for j in range(1, len(u_list)):
            if u_list[j] < u_list[i]:
                i = j

        new_list.append(u_list.pop(i))

    return new_list


print(f'sorted list: {selection_sort([0, -1, 4, 3, 4, 10, 1])}')

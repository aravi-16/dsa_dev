def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num>largest:
            largest = num
    return largest
print(find_largest([3,13,21,9,2]))

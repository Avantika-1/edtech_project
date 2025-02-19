#Program list1 = [2,3,4,5,6,3,2], sum = 8.
# Sum of 2 elements in list should be given sum.
# output for given example list :[(2,6),(3,5)]
def find_pairs(lst, target_sum):
    pairs = []
    seen = set()

    for num in lst:
        complement = target_sum - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)

    return pairs


# Example usage:
list1 = [2, 3, 4, 5, 6, 3, 2]
target_sum = 8
print(find_pairs(list1, target_sum))

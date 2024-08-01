def reverse_list(nums):
    for i in range(len(nums) - 1, -1, -1):
        yield nums[i]
print (list(reverse_list([1, 2, 3, 4, 5, 6, 7])))


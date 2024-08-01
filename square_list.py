
def square_list(nums):
  for i in range(len(nums)):
    nums[i]= nums[i]**2

num_list = [2, 4, 5, 6, 7]
square_list(num_list)
print(num_list)
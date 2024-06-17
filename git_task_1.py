from functools import reduce
nums = list(map(int, input().split()))

print(nums)
sum_of_lst = lambda lst: sum(lst)
mult_of_lst = reduce(lambda x, y: x * y, nums) 

print(sum_of_lst(nums))
print(mult_of_lst)


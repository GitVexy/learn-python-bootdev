def divide_list(nums, divisor):
    if divisor == 0:
        raise ZeroDivisionError("ERROR: Cannot divide by zero!")
    if type(nums) != list:
        raise TypeError(f"ERROR: divide_list expected populated list, but got: {nums} of type {type(nums)}")
    if nums == []:
        print(f"Warning: divide_list expected populated list, but got {nums}")
        return nums
    
    out = []
    for num in nums:
        out.append(num / divisor)
    return out

print(divide_list([10, 20, 30], 10))
print(divide_list([], 5))
print(divide_list("not a list", 3))

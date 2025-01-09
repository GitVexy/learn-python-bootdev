def remove_nonints(nums):
    out = []
    for num in nums:
        if type(num) == int:
            out.append(num)
    return out
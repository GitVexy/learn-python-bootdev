def find_min(nums):
    small = float("inf")
    
    for n in nums:
        if n < small:
            small = n
            
    return small
def removeDuplicates(nums):
    if not nums:  # Edge case: empty list
        return 0
    
    slow = 0  # Tracks the position for the next unique element
    
    for fast in range(1, len(nums)):  # Start from the second element
        if nums[fast] != nums[slow]:   # Found a new unique element!
            slow += 1
            nums[slow] = nums[fast]    # Move it to the correct position
    
    return slow + 1  # Number of unique elements


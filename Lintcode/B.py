'''
@return index of target, if found, or -1 if not found
'''
def binarySearch(nums, target):
    first = 0
    last = len(nums) - 1
    while first < last:
        midpoint = (first + last) // 2
        if nums[midpoint] == target:
            return midpoint
        elif target < nums[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return -1

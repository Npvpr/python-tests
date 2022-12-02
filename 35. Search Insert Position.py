def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    tmpList = nums[:]
    while True:
        lenTmp = len(tmpList)
        half = lenTmp//2
        halfNum = tmpList[half]
        if halfNum == target:
            return nums.index(halfNum)
        elif lenTmp == 1:
            i = nums.index(halfNum)
            if halfNum > target:
                if i == 0:
                    return 0
                return i-1
            elif halfNum < target:
                return i+1
        elif tmpList[half] > target:
            tmpList = tmpList[:half]
        elif tmpList[half] < target:
            tmpList = tmpList[half:]
                
print(searchInsert(nums = [1,3,5,6], target = 5))
print(searchInsert(nums = [1,3,5,6], target = 2))
print(searchInsert(nums = [1,3,5,6], target = 7))
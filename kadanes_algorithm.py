print("This file will show how we implement Kadane's algorithm to find the max/min contiguous subarray sum of a list.")

def find_max_con_sub_sum(nums):
    # check the input type, if not list, show TypeError
    if type(nums) is not list:
        raise TypeError("Invalid input for the function")

    maxSum = float('-inf')
    currSum = 0

    for num in nums:
        if currSum < 0:
            currSum = 0
        currSum += num
        maxSum = max(maxSum, currSum)

    return maxSum

def find_min_con_sub_sum(nums):
    # check the input type, if not list, show TypeError
    if type(nums) is not list:
        raise TypeError("Invalid input for the function")

    minSum = float('inf')
    currSum = 0

    for num in nums:
        if currSum > 0:
            currSum = 0
        currSum += num
        minSum = min(minSum, currSum)

    return minSum




from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # No solution found


class Solution:
    List = [1, 23, 4, 4, 5, 2]
    print(twoSum(List, 24))




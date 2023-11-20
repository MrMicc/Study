from collections import defaultdict
from typing import List


class LongestConsecutive():
    """docstring for LongestConsecutive."""

    def __init__(self, nums: List[int]):
        self.__nums = nums

    def get_longest_length(self) -> int:
        nums = self.__nums

        if len(nums) == 0:
            return 0

        nums = list(set(nums))  # remove duplicate
        nums.sort()
        max_count = 1
        count = 1
        for index in range(1, len(nums)):
            if nums[index] == nums[index-1] + 1:  # numbers are consecutive
                count += 1
            else:
                # max count of consecutive numbers
                max_count = max(max_count, count)
                count = 1

        return max(max_count, count)

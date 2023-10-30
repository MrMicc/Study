from typing import List

class TwoSum:

    def __init__(self, nums: List[int]):
        self.nums = nums;

    def get_sum(self, target: int) -> List[int]:
        self._is_more_then_one();
        resultMap = {};
        for index, num in enumerate(self.nums):
            diff = target - num; #geeting the difference between the target and the current number
            if diff in resultMap: #if the difference is already in the map then get the index off it and return the acutal index
                return [resultMap[diff], index];

            #if not then put the current index and the current number in the map
            resultMap[num] = index; 

        return [];

    def _is_more_then_one(self) -> bool:
        if len(self.nums) <= 1:
            raise ValueError("Need more then one element in array");
        
        return True

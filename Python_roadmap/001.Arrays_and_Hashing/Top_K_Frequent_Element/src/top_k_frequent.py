from typing import List


class TopKFrequent:

    def top(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        # create a array of list, each list has 2 elements, 1st is the value, 2nd is the frequence
        frequence = [[] for i in range(len(nums)+1)]
        for num in nums:
            # update the frequence of the number
            seen[num] = seen.get(num, 0)+1
        for n, c in seen.items():  # put the number and its frequence into the array
            frequence[c].append(n)
        result = []
        # iterate the array from the end to the begining
        for i in range(len(frequence)-1, 0, -1):
            for num in frequence[i]:  # iterate the list in the frequence array
                result.append(num)
                if len(result) == k:  # if the length of the result is the same as the k, then stop
                    return result

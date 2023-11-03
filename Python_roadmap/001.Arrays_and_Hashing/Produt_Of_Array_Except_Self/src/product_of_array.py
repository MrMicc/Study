from typing import List;

class ProductOfArray:

    def product_of_array(self, nums: List[int]) -> List[int]:
        result = [];
        for index in range(len(nums)):
            aux = 1;
            for multiplier in range(len(nums)):
                if index != multiplier:
                    aux *= nums[multiplier];
            result.append(aux);

        return result;


    def product_except_self(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums); # create a list with the same size of nums

        prefix = 1; # prefix is a variable that is used to store the product of all numbers except the current index
        for index in range(len(nums)):
            result[index] = prefix; # assign the current product to the current index
            prefix *= nums[index]; # multiply the prefix with the current number
        postfix = 1; # postfix is a variable that is used to store the product of all numbers except the current index
        for index in range(len(nums) - 1, -1, -1): # iterate in reverse order
            result[index] *= postfix; # multiply the current product with the postfix
            postfix *= nums[index]; # multiply the postfix with the current number
        return result;



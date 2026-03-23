 
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for x in range (i+1,(len(nums))):
                if ((nums[i] + nums[x]) == target):
                    return [i,x]

                    # Note that this uses 0(n2) and the best soolution would require 0(n) but
                    # for the first straight think this is ok

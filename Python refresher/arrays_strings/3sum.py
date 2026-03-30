class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # we will have three points and all added should be
        # = to 0, so x+y+z=0 y+z = -x
        output = []
        nums.sort()
        for index, value in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            result = -value
            left = index + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right]
                if total == result:
                    ans = [value, nums[left], nums[right]]
                    output.append(ans)
                    left += 1
                    right -= 1
                    # Skip duplicates on left side
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates on right side
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total > result:
                    right -= 1
                elif total < result:
                    left += 1
        return output

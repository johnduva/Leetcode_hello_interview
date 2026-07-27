class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        currZero = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[currZero], nums[i] = nums[i], nums[currZero]
                currZero+=1
        return nums

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        un = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1]:
                nums[un] = nums[i]
                un += 1
        return un
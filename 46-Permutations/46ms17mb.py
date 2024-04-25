class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]


        o = []

        for x in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for p in perms:
                p.append(n)
            
            o.extend(perms)
            nums.append(n)
        
        return o
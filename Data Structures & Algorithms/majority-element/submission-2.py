class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = ans = 0
        for val in nums:
            if x==0:
                ans=val
            x+= 1 if val == ans else -1
        return ans
            
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        extended_nums=nums
        for i in range(len(nums)):
            extended_nums.append(nums[i])
        return extended_nums

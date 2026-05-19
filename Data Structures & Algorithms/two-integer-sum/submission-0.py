class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if hashmap.get(diff) is not None:
                return [hashmap[diff], i]
            hashmap[nums[i]]=i
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for x in nums:
            hashmap[x]+=1
        for y in hashmap.keys():
            if hashmap[y]>len(nums)/2:
                return y


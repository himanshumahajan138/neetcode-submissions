class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for x in strs:
            hashtable = [0]*26
            for y in x:
                hashtable[ord(y) - ord('a')]+=1
            hashmap[tuple(hashtable)].append(x)
        return list(hashmap.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = {}
        for s in strs:
            anagram = "".join(sorted(s))
            if anagram not in sortedStrs:
                sortedStrs[anagram] = [s]
            else: 
                sortedStrs[anagram].append(s)
            
        return list(sortedStrs.values())
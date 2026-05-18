from collections import Counter 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_t = {}
        for word in strs:
            if("".join(sorted(word)) in hash_t):
                hash_t["".join(sorted(word))].append(word)
            else:
                hash_t["".join(sorted(word))] = [word]
        
        return list(hash_t.values())



        
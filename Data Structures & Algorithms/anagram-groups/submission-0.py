class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash = {}

        for str in strs:

            sortedStr = tuple(sorted(str))

            if sortedStr in hash:

                hash[sortedStr].append(str)

            else:

                hash[sortedStr] = [str]

        return list(hash.values())
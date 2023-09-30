from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map: dict[str, list[str]] = {}
        for s in strs:
            key: str = ''.join(sorted(s))
            if key in map:
                map[key].append(s)
            else:
                map[key] = [s]
        return list(map.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams(strs))

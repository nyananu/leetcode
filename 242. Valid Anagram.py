class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # take s and t and put it in a map with letter occurance
        # determine if equal
        s_map = {}
        for c in s:
            if c in s_map:
                s_map[c] += 1
            else:
                s_map.update({ c : 1 })
        
        t_map = {}
        for l in t:
            if l in t_map:
                t_map[l] += 1
            else:
                t_map.update({ l : 1 })

        return (s_map == t_map)
        

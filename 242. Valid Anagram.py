class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Option 1
        s = sorted(s)
        t = sorted(t)

        return (s == t)
         
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)
        
        xxxxxxxxxxxxxxxxxxxxxxxxxxx

        # Option 2
        s_map = {}
        t_map = {}

        for c in s:
            if c not in s_map:
                s_map[c] = 1
            else:
                s_map[c] += 1
        
        for m in t:
            if m not in t_map:
                t_map[m] = 1
            else:
                t_map[m] += 1
        
        return (s_map == t_map)

            # Time Complexity: O(n)
            # Space Complexity: O(n)
            # Here we are using 2 maps
    
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    # Option 3
            
            if (len(s) != len(t)):
                return False
    
            s_map = Counter(s)
            
            for c in t:
                if c not in s_map:
                    return False
                if (c in s_map and s_map[c] > 0):
                    s_map[c] -= 1
                else:
                    return False
            return True
            
            # Time Complexity: O(n)
            # Space Complexity: O(n)
            # Advantage is that we are using 1 map to check the anagram instead of 2


    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

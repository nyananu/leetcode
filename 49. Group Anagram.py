class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        res = []

        # for each word, sort the letters in alphabetical order
        for word in strs:
            sorted_letters = ("").join(sorted(word))

            # if that sorted word is not in the map, add it with the value being the curr word. Otherwise just append to that list of val
            # {'aet': ['eat', 'tea'], 'ant': ['tan']}

            if sorted_letters not in anagram_map:
                anagram_map[sorted_letters] = [word]

            else:
                anagram_map[sorted_letters].append(word)

            # for all the values in the anagram_map, append them into a result List.
        for val in anagram_map.values():
            res.append(val)
        return res

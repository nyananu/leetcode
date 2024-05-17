class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # go through the array and put in map the curr_num as key and its freq as value.
        # whichever key has highest value, return that key

        freq_map = {}

        for num in nums:
            # if curr num already in map, update the freq; otherwise add to map
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
# freq_map.get: This part is used as the key function for sorting. It tells the sorted() function to use the values of the dictionary (frequencies) as the basis for sorting the keys.

# sorted(...): This function sorts the keys of the dictionary based on their corresponding values from highest to lowest because reverse=True is specified.

# reverse=True: This argument specifies that the sorting should be in descending order (highest value first).

# [:k]: This is a slicing operation that selects the first k elements from the sorted list of keys. These are the keys associated with the top k highest frequencies.
        top_k_freq = sorted(freq_map, key=freq_map.get, reverse=True)[:k]

        return top_k_freq

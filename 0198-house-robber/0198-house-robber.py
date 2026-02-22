class Solution:
    def rob(self, nums: List[int]) -> int:
        total_houses = len(nums)
        max_loot_cache = [-1]*total_houses
        
        def loot_from(house_number):
            if house_number >= total_houses:
                return 0
            if max_loot_cache[house_number] != -1:
                return max_loot_cache[house_number]
            steal = nums[house_number]+loot_from(house_number+2)
            skip = loot_from(house_number+1)
            max_loot_cache[house_number] = max(skip, steal)
            return max_loot_cache[house_number] 

        return loot_from(0)


        
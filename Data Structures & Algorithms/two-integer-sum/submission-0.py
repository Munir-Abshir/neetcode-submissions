class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_t = {}
        for i in range(len(nums)):
            if((target - nums[i]) in hash_t):
                return [hash_t[(target - nums[i])],i]
            hash_t[nums[i]] = i
        
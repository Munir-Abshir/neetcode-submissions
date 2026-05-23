class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res






        # brute force solutuon that works!
        # res = []
        # for i in range(len(nums)):
        #     sums = 1
        #     for j in range(len(nums)):
        #         if(j!= i):
        #             sums *= nums[j]
        #     res.append(sums)
        # return res


            
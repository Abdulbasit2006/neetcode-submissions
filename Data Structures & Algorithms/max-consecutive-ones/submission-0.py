class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count_now = 0 
        max_count_so_far = 0 

        for i in nums:
            if i == 1:
                max_count_now += 1
            else:
                max_count_so_far =max(max_count_now, max_count_so_far) 
                max_count_now = 0
        
        max_count_so_far =max(max_count_now, max_count_so_far)
        return max_count_so_far

        
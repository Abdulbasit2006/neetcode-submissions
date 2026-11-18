class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = []
        val_counter= 0
        for i in range(len(nums)):
            val= nums[i]
            for i in nums:
               
                if val == i:
                    val_counter= val_counter+1
                    if val_counter > (len(nums)/2):
                        return val

    

        
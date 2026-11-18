class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #we have a sorted array with duplicate values
        # we will use two pointers to keep track of the array 
        # r pointer will traverse the whole array 
        # r pointer will also compare two adhacent values to check if 
        # are different 
        # l pointer will always point to the position that a new unique value can be inserted in
        #
        l=1
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l=l+1
        return l

            

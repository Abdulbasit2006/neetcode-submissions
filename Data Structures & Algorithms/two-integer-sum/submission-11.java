class Solution {
    int[] indexes;
    public int[] twoSum(int[] nums, int target) {
        for(int i = 0; i<=nums.length-1; i++){
            for(int j = i+1; j<=nums.length-1; j++){
                if((nums[i]+nums[j])==target){
                    indexes= new int[2];
                    indexes[0]=i;
                    indexes[1]=j;
                    return indexes;

                }
            } 
        }
        return new int[]{};
        
    }
}


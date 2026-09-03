class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        let l = 0;
        let r = nums.length - 1;

        let mid = Math.floor((r - l) / 2);
        let i = 0;
        while(l != r && l < r){

            if(nums[mid] >= nums[r]){
                l = mid + 1;
            }else{
                r = mid;
            }

            mid = l + Math.floor((r - l) / 2);
        }

        return nums[mid];
    }
}

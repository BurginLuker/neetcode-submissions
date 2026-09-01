class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        nums.sort((a, b) => a - b);
        let out = [];

        for (let i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] === nums[i - 1]) continue;
            if (nums[i] > 0) break; // sorted array, can't sum to 0 anymore

            let l = i + 1;
            let r = nums.length - 1;
            let target = 0 - nums[i];

            while (l < r) {
                let curr = nums[l] + nums[r];

                if (curr === target) {
                    out.push([nums[i], nums[l], nums[r]]);
                    l++;
                    r--;
                    while (l < r && nums[l] === nums[l - 1]) l++;
                    while (l < r && nums[r] === nums[r + 1]) r--;
                } else if (curr < target) {
                    l++;
                } else {
                    r--;
                }
            }
        }

        return out;
    }
}
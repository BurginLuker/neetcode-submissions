class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const numset = new Set([...nums]);
        return numset.size != nums.length;
    }
}

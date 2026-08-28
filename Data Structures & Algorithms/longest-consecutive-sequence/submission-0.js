class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let numSet = new Set(nums);

        let max = 0;
        for(let n of numSet){
            if(numSet.has(n - 1)){
                continue;
            }

            let count = 0;
            while(numSet.has(n)){
                count++;
                n++;
            }

            max = Math.max(count, max);
        }

        return max;
    }
}

class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let max = 0;

        let left = 0;
        let right = heights.length - 1;

        while(left < right){
            let smaller = Math.min(heights[left], heights[right]);
            let area = smaller * (right - left);
            max = Math.max(area, max);

            if(heights[left] > heights[right]){
                right--;
            }else{
                left++;
            }
        }

        return max;
    }
}

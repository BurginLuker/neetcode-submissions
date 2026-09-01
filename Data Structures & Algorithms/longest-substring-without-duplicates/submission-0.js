class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let max = 0;

        let left = 0;
        let chars = new Set();
        for(let i = 0; i < s.length; i++){
            while(chars.has(s[i])){
                chars.delete(s[left]);
                left++;
            }

            chars.add(s[i]);
            max = Math.max(chars.size, max);
        }

        return max;
    }
}

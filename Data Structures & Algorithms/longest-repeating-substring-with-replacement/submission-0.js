class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        let max = 0;
        let left = 0;

        let freq = new Map();
        let maxFreq = 0;

        for (let i = 0; i < s.length; i++) {
            freq.set(s[i], (freq.get(s[i]) || 0) + 1);
            maxFreq = Math.max(maxFreq, freq.get(s[i]));

            let windowSize = i - left + 1;
            while (windowSize - maxFreq > k) {
                freq.set(s[left], freq.get(s[left]) - 1);
                left++;
                windowSize = i - left + 1;
            }

            max = Math.max(windowSize, max);
        }

        return max;
    }
}

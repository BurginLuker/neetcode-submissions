class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let freq = new Map();

        for(const c of s){
            freq.set(c, (freq.get(c) || 0) + 1);
        }

        for(const c of t){
            freq.set(c, (freq.get(c) || 0) - 1);
        }

        return freq.values().every((s) => s == 0);
    }
}

class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s, t) {
        if (t.length === 0 || s.length === 0) return "";

        let subFreqs = {};
        for (let i = 0; i < t.length; i++) {
            subFreqs[t[i]] = (subFreqs[t[i]] || 0) + 1;
        }

        const required = Object.keys(subFreqs).length;

        let freqs = {};
        let valid = 0;
        let left = 0;

        let min = Infinity;
        let str = "";

        for (let i = 0; i < s.length; i++) {
            freqs[s[i]] = (freqs[s[i]] || 0) + 1;
            if (subFreqs[s[i]] !== undefined && freqs[s[i]] === subFreqs[s[i]]) {
                valid++;
            }

            while (valid === required) {
                if (i - left + 1 < min) {
                    min = i - left + 1;
                    str = s.substring(left, i + 1);
                }

                freqs[s[left]] = freqs[s[left]] - 1;
                if (subFreqs[s[left]] !== undefined && freqs[s[left]] < subFreqs[s[left]]) {
                    valid--;
                }
                left++;
            }
        }

        return str;
    }
}
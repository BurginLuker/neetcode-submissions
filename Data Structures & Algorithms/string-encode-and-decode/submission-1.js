class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        return strs.map(s => `${s.length}-${s}`).join('')
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let left = 0;
        let out = [];
        console.log(str);
        while(left < str.length){
            let right = left;
            while(str[right] !== '-'){
                right++;
            }

            let length = parseInt(str.substring(left, right));
            let start = right + 1;
            left = start + length;
            out.push(str.substring(start, left));
        }

        return out;
    }
}

class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let map = new Map();

        for(const s of strs){
            let freq = new Array(26).fill(0);
            
            for(const l of s){
                freq[l.charCodeAt() % 26] += 1;
            }

            let key = JSON.stringify(freq);
            let current = map.get(key) || [];

            current.push(s);
            map.set(key, current);
        }
        
        return Array.from(map.values());
    }
}

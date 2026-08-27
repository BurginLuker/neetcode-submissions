class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let max = Math.max(...nums);

        let freq = new Map();

        for(const n of nums){
            freq.set(n, (freq.get(n) || 0) + 1);
        }

        let buckets = Array.from({length: Math.max(...Array.from(freq.values())) + 1}, () => []);

        for(const [n, f] of freq.entries()){
            buckets[f].push(n);
        }


        let out = [];
        for(let i = buckets.length - 1; i >= 0 && out.length < k; i--){
            out = out.concat(buckets[i]);
        }

        return out;
    }
}

class Solution {
    /**
     * @param {string} blocks
     * @param {number} k
     * @return {number}
     */
    minimumRecolors(blocks, k) {
        let l = 0;

        let ws = 0;
        for (let i = 0; i < k; i++) {
            if (blocks[i] == "W") {
                ws++;
            }
        }

        let min = ws;
        for (let i = k; i < blocks.length; i++) {
            if (blocks[i - k] == "W") {
                ws--;
            }
            if (blocks[i] == "W") {
                ws++;
            }

            min = Math.min(min, ws);
        }

        return min;
    }
}

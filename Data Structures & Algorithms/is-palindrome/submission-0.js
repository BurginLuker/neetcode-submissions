class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        function isAlphanumeric(str) {
            return /^[a-z0-9]+$/i.test(str);
        }
        s = s.split("").filter((c) => isAlphanumeric(c)).map(c => c.toLowerCase()).join('');

        let left = 0;
        let right = s.length - 1;

        while(left < right){

            if(s[left] !== s[right]){
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}

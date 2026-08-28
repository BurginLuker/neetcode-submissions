class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let leftProds = new Array(nums.length).fill(0);
        let rightProds = new Array(nums.length).fill(0);

        let prod = 1;
        for(let i = 0; i < nums.length - 1; i++){
            prod *= nums[i];
            leftProds[i + 1] = prod;
        }

        prod = 1;
        for(let i = nums.length - 1; i > 0; i--){
            prod *= nums[i];
            rightProds[i - 1] = prod;
        }
       
        let out = [];
        out.push(rightProds[0]);

        for(let i = 1; i < nums.length - 1; i++){
            let left = leftProds[i];
            let right = rightProds[i];

            out.push(left * right);
        }

        out.push(leftProds[nums.length - 1]);

        return out;;
    }
}

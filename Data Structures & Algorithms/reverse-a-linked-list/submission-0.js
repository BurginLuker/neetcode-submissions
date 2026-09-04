/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head) {
        let prev = null;
        let iter = head;

        while(iter){
            let temp = iter.next;

            iter.next = prev;
            prev = iter;

            iter = temp;
        }

        return prev;
    }
}

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
         HashSet<ListNode> unique = new HashSet<>();
         if (head == null){
            return false;
         }
         ListNode curr = head;
         while (curr != null){
            if (unique.contains(curr)){
                return true;
            }
            unique.add(curr);
            curr = curr.next;
         }
         return false;
    }
}

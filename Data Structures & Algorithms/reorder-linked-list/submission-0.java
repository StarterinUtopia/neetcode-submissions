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
    public void reorderList(ListNode head) {

        if (head == null || head.next == null){
            return;
        }
        ListNode fast = head;
        ListNode slow = head;
        //1.find the middle point
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        //2.reverse the latter half.
        ListNode prev = null;
        ListNode second = slow.next;
        slow.next = null;

        while (second != null){
            ListNode nextTemp = second.next;
            second.next = prev;
            prev = second; 
            second = nextTemp;
        }
        //3.merge two list
        ListNode first = head;
        second = prev;//head of the reversed half

        while (second != null){
            ListNode temp1 = first.next;
            ListNode temp2 = second.next;

            first.next = second;
            second.next = temp1;

            first = temp1;
            second = temp2;
        }
    }
}

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        return add(l1,l2,0);
    }
    ListNode* add(ListNode* l1, ListNode* l2,int carry) {
        int x = 0;
        int y = 0;
        ListNode* next1 = nullptr;
        ListNode* next2 = nullptr;
        if (l1 != nullptr) {
            x = l1->val;
            next1 = l1->next;
        }
        if (l2 != nullptr) {
            y = l2->val;
            next2 = l2->next;
        }
        if (l1 == nullptr && l2 == nullptr && carry ==0) {
            return nullptr;
        }
        int sum = x+y+carry;
        ListNode* node = new ListNode(sum%10);
        node->next = add(next1,next2,sum/10);
        return node;
    }
};

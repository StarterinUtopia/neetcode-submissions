/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        std::pmr::unordered_map<Node* , Node*>copies;
        Node* cur = head;
        if (head == nullptr) {
            return nullptr;
        }
        while (cur != nullptr) {
            copies[cur] = new Node(cur->val);
            cur = cur->next;
        }
        cur = head;
        while (cur->next != nullptr) {
            Node* copy = copies[cur];
            copy->next = copies[cur->next];
            cur = cur->next;
        }
        cur = head;
        while (cur !=nullptr) {
            Node* copy = copies[cur];
            if (cur->random != nullptr) {
                copy->random = copies[cur->random];
            }
            cur = cur->next;
        }
        return copies[head];
    }
};

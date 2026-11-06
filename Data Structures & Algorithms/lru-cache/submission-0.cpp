class Node {
public:
    int key;
    int val;
    Node* next;
    Node* prev;

    Node(int _key,int _val) {
        key = _key;
        val = _val;
        next = nullptr;
        prev = nullptr;
    }
};
class LRUCache {
private:
    unordered_map<int, Node*> cache;
    int cap;
    Node* dummy;
    void detach(Node* node) {
        Node* prev = node->prev;
        Node* next = node->next;
        prev->next = next;
        next->prev = prev;
    }
    void pushFront(Node* node) {
        Node* first = dummy->next;
        node->next = first;
        first->prev = node;
        dummy->next = node;
        node->prev = dummy;
    }
public:
    LRUCache(int capacity) {
        cap = capacity;
        dummy = new Node(0,0);
        dummy ->prev = dummy;
        dummy ->next = dummy;
    }
    ~LRUCache() {
        Node* cur = dummy->next;
        while (cur != dummy) {
            Node* next = cur->next;
            delete cur;
            cur = next;
        }
        delete dummy;
    }

    int get(int key) {
        if (cache.count(key) == 0) {
            return -1;
        }
        Node* node= cache[key];
        detach(node);
        pushFront(node);
        return node->val;
    }

    void put(int key, int value) {
        if (cache.count(key) != 0) {
            Node* node =cache[key];
            detach(node);
            pushFront(node);
            node->val = value;
        }
        else {
            Node* node = new Node(key,value);
            pushFront(node);
            cache[key] = node;
        }
        if (cache.size() > cap) {
            Node* oldest = dummy->prev;
            detach(oldest);
            cache.erase(oldest->key);
            delete oldest;
        }
    }
};

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (head == nullptr) return nullptr;
        unordered_set<ListNode*> node_set;
        node_set.insert(head);
        while (head->next != nullptr) {
            if (node_set.find(head->next) == node_set.end()) node_set.insert(head);
            else return head->next;
            head = head->next;
        }
        return nullptr;
    }
};

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
    ListNode* partition(ListNode* head, int x) {
        if (head == nullptr || head->next == nullptr) return head;
        ListNode* answer = nullptr;
        ListNode* insert_node;
        ListNode* node = head;
        ListNode* change_node;
        if (node->val < x) {
            answer = node;
            insert_node = answer;
        }
        while (node->next != nullptr) {
            cout << node->next->val << endl;
            if (node->next->val < x) {
                if (answer == nullptr) {
                    answer = node->next;
                    node->next = node->next->next;
                    answer->next = head;
                    insert_node = answer;
                }
                else if (insert_node != node) {
                    change_node = node->next;
                    node->next = change_node->next;
                    change_node->next = insert_node->next;
                    insert_node->next = change_node;
                    insert_node = insert_node->next;
                }
                else {
                    insert_node = insert_node->next;
                    node = node->next;
                }
            }
            else node = node->next;
        }
        if (answer == nullptr) return head;
        return answer;
    }
};

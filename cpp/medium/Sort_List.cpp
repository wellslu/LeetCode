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
    ListNode* sortList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;

        // vector<ListNode*> node_list;
        // node_list.push_back(head);
        // int idx;
        // while (head->next != nullptr) {
        //     idx = node_list.size();
        //     head = head->next;
        //     node_list.push_back(head);
        //     while (idx > 0 && node_list[idx]->val < node_list[idx-1]->val) {
        //         swap(node_list[idx], node_list[idx-1]);
        //         idx--;
        //     }
        // }

        vector<int> num_list;
        num_list.push_back(head->val);
        while (head->next != nullptr) {
            head = head->next;
            num_list.push_back(head->val);
        }
        sort(num_list.begin(), num_list.end());
        
        // ListNode* ans = node_list[0];
        // ListNode* node = ans;
        // for (int i = 1; i < node_list.size(); ++i) {
        //     node->next = node_list[i];
        //     node = node->next;
        // }
        // node->next = nullptr;

        ListNode* ans = new ListNode(num_list[0]);
        ListNode* node = ans;
        for (int i = 1; i < num_list.size(); ++i) {
            node->next = new ListNode(num_list[i]);
            node = node->next;
        }

        return ans;
    }
};

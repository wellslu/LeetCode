/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 /**
 x = 原點道迴圈起始點，y = 迴圈起始點到meet點
2 steps 追上 1 step 時分別走了 => 2(x+y), (x+y)，所以1 step只要在走x+y步一樣可回到meet點，走y步會等於從迴圈起始點到meet點，所以只要再走x步就會到迴圈起始點
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        // if (head == nullptr) return nullptr;
        // unordered_set<ListNode*> node_set;
        // node_set.insert(head);
        // while (head->next != nullptr) {
        //     if (node_set.find(head->next) == node_set.end()) node_set.insert(head);
        //     else return head->next;
        //     head = head->next;
        // }
        // return nullptr;
        if (head == nullptr || head->next == nullptr || head->next->next == nullptr) return nullptr;
        ListNode *fast = head->next->next;
        ListNode *slow = head->next;
        while(fast != slow) {
            if (fast->next == nullptr || fast->next->next == nullptr) return nullptr;
            fast = fast->next->next;
            slow = slow->next;
        }
        while(head != slow) {
            head = head->next;
            slow = slow->next;
        }
        return head;
    }
};

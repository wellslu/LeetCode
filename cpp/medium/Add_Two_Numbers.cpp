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
        int overflow = 0;
        int sum = l1->val + l2->val + overflow;
        if (sum >= 10) {
            overflow = 1;
            sum -= 10;
        }
        else overflow = 0;
        ListNode* answer = new ListNode(sum);
        ListNode* next_answer = answer;
        while (l1->next or l2->next) {
            if (l1->next and l2->next) {
                l1 = l1->next;
                l2 = l2->next;
                sum = l1->val + l2->val + overflow;
            }
            else if (l1->next) {
                l1 = l1->next;
                sum = l1->val + overflow;
            }
            else {
                l2 = l2->next;
                sum = l2->val + overflow;
            }
            if (sum >= 10) {
                overflow = 1;
                sum -= 10;
            }
            else overflow = 0;
            next_answer->next = new ListNode(sum);
            next_answer = next_answer->next;
        }
        if (overflow) {
            next_answer->next = new ListNode(overflow);
        }
        return answer;
    }
};
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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr) return head;
        int length = 1;
        ListNode* next_head = head;
        ListNode* answer;
        while(next_head->next != nullptr) {
            ++length;
            next_head = next_head->next;
        }
        next_head->next = head;
        while(k >= length) k-=length;
        for(int i = 0; i <= length-k-1; i++) {
            next_head = next_head->next;
        }
        answer = next_head->next;
        next_head->next = nullptr;
        return answer;
    }
};

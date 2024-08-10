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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        if(head == nullptr) return nullptr;

        vector<TreeNode*> node_list;
        TreeNode* node_head;
        TreeNode* node;
        node_head = new TreeNode(head->val);
        head = head->next;
        int cnt = 1;
        while (head != nullptr) {
            node = new TreeNode(head->val);
            node->left = node_head;
            node_head = node;
            head = head->next;
            cnt++;
        }

        if (cnt <= 2) return node_head;
        TreeNode* root = divide_conquer(node_head, cnt);

        return root;
    }
    TreeNode* divide_conquer(TreeNode* node_head, int cnt) {
        if (cnt <= 2) return node_head;
        TreeNode* right_root = node_head;
        int mid = cnt / 2;
        if (mid % 2 == 0) mid--;
        for (int i = 0; i < mid - 1; ++i) {
            node_head = node_head->left;
        }
        TreeNode* root = node_head->left;
        node_head->left = nullptr;
        root->right = divide_conquer(right_root, mid);
        root->left = divide_conquer(root->left, cnt - mid - 1);
        return root;
    }
};

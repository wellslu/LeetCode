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
    int ans = 0;
    int sumNumbers(TreeNode* root) {
        if (root == nullptr) return 0;
        next_node(root, 0);
        return ans;
    }
    void next_node(TreeNode* node, int num) {
        num = num * 10 + node->val;
        if (node->left == nullptr && node->right == nullptr) ans+=num;
        if (node->left !=nullptr) next_node(node->left, num);
        if (node->right !=nullptr) next_node(node->right, num);
    }
};

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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        if (root == nullptr) return ans;
        next_level(root, ans);
        return ans;
    }
    void next_level(TreeNode* node, vector<int>& ans) {
        ans.push_back(node->val);
        if (node->left != nullptr) {
            next_level(node->left, ans);
        }
        if (node->right != nullptr) {
            next_level(node->right, ans);
        }
    }
};

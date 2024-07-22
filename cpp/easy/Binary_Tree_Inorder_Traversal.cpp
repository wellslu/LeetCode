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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans;
        if (root == nullptr) return ans;
        next_level(root, ans);
        return ans;
    }
    void next_level(TreeNode* root, vector<int>& ans) {
        if (root->left != nullptr) {
            if (root->left->left != nullptr) next_level(root->left->left, ans);
            ans.push_back(root->left->val);
            if (root->left->right != nullptr) next_level(root->left->right, ans);
        }
        ans.push_back(root->val);
        if (root->right != nullptr) {
            if (root->right->left != nullptr)next_level(root->right->left, ans);
            ans.push_back(root->right->val);
            if (root->right->right != nullptr)next_level(root->right->right, ans);
        }
    }
};

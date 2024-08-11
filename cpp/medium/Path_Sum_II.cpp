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
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> ans;
        if (root == nullptr) return ans;
        vector<int> comb;
        next_node(root, targetSum, 0, comb, ans);
        return ans;
    }
    void next_node(TreeNode* node, int targetSum, int current_sum, vector<int>& comb, vector<vector<int>>& ans) {
        comb.push_back(node->val);
        if (node->left == nullptr && node->right == nullptr) {
            if (current_sum + node->val == targetSum) {
                ans.push_back(comb);
            }
        }
        if (node->left != nullptr) {
            next_node(node->left, targetSum, current_sum + node->val, comb, ans);
            comb.pop_back();
        }
        if (node->right != nullptr) {
            next_node(node->right, targetSum, current_sum + node->val, comb, ans);
            comb.pop_back();
        }
    }
};

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if (root != nullptr) next_node(root, ans, 0);
        return ans;
    }
    void next_node(TreeNode* node, vector<vector<int>>& ans, int level) {
        if (ans.size() <= level) {
            vector<int> comb{node->val};
            ans.push_back(comb);
        }
        else ans[level].push_back(node->val);
        if(node->left != nullptr) next_node(node->left, ans, level+1);
        if(node->right != nullptr) next_node(node->right, ans, level+1);
    }
};

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
    bool isValidBST(TreeNode* root) {
        vector<int> left;
        vector<int> right;
        return nextNode(root, left, right);
    }
    bool nextNode(TreeNode* node, vector<int>& left, vector<int>& right) {
        for (auto i:left) {
            if (node->val >= i) return false;
        }
        for (auto i:right) {
            if (node->val <= i) return false;
        }
        if (node->left != nullptr) {
            left.push_back(node->val);
            if (!nextNode(node->left, left, right)) return false;
            left.pop_back();
        }
        if (node->right != nullptr) {
            right.push_back(node->val);
            if (!nextNode(node->right, left, right)) return false;
            right.pop_back();
        }
        return true;
    }
};

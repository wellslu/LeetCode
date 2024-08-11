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
    void flatten(TreeNode* root) {
        if (root != nullptr) next_node(root);
    }
    void next_node(TreeNode* node) {
        cout << node->val << endl;
        TreeNode* left_node = node->left;
        TreeNode* right_node = node->right;
        node->right = nullptr;
        if (left_node != nullptr) {
            node->right = left_node;
            node->left = nullptr;
            next_node(left_node);
        }
        if (right_node != nullptr) {
            while (node->right != nullptr) node = node->right;
            node->right = right_node;
            next_node(right_node);
        }
    }
};

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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (root == nullptr) return vector<vector<int>> {};
        vector<vector<int>> ans{vector<int> {root->val}};
        vector<TreeNode*> queue{root};
        next_node(ans, queue);
        return ans;
    }
    void next_node(vector<vector<int>>& ans, vector<TreeNode*>& queue) {
        vector<int> comb;
        vector<TreeNode*> next_queue;
        if (ans.size() % 2 == 0) {
            for(auto q:queue) {
                if (q->left != nullptr) {
                    comb.push_back(q->left->val);
                    next_queue.push_back(q->left);
                }
                if (q->right != nullptr) {
                    comb.push_back(q->right->val);
                    next_queue.push_back(q->right);
                }
            }
        }
        else {
            for(auto q:queue) {
                if (q->right != nullptr) {
                    comb.push_back(q->right->val);
                    next_queue.push_back(q->right);
                }
                if (q->left != nullptr) {
                    comb.push_back(q->left->val);
                    next_queue.push_back(q->left);
                }
            }
        }
        if (next_queue.size() > 0) {
            reverse(next_queue.begin(), next_queue.end());
            ans.push_back(comb);
            next_node(ans, next_queue);
            }
    }
};

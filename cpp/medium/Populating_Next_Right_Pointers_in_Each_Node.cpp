/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        vector<Node*> queue{root};
        next_level(queue);
        return root;
    }
    void next_level(vector<Node*>& queue) {
        Node* node = nullptr;
        vector<Node*> next_queue;
        // cout << queue[0]->val << endl;
        for (auto q:queue) {
            if (q && q->left != nullptr) {
                if (node == nullptr) node = q->left;
                else {
                    node->next = q->left;
                    node = node->next;
                }
                next_queue.push_back(q->left);
            }
            if (q && q->right != nullptr) {
                if (node == nullptr) node = q->right;
                else {
                    node->next = q->right;
                    node = node->next;
                }
                next_queue.push_back(q->right);
            }
        }
        if (next_queue.size() != 0) next_level(next_queue);
    }
};

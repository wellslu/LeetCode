/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr) return nullptr;
        queue<Node*> q;
        unordered_map<int, Node*> already_map;
        Node* ans_node = new Node(node->val);
        already_map[ans_node->val] = ans_node;
        q.push(node);
        while (!q.empty()) {
            Node* n = q.front();
            q.pop();
            Node* new_n_node = already_map.find(n->val)->second;
            for (auto neighbor:n->neighbors) {
                if (already_map.find(neighbor->val) == already_map.end()) {
                    Node* new_node = new Node(neighbor->val);
                    already_map[new_node->val] = new_node;
                    q.push(neighbor);
                }
                new_n_node->neighbors.push_back(already_map.find(neighbor->val)->second);
            }
        }
        return ans_node;
    }
};

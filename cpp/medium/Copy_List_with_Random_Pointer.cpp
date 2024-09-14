/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr) return head;
        Node* ans = new Node(head->val);
        Node* new_node = ans;
        Node* node = head;
        vector<Node*> new_node_list{ans};
        vector<Node*> node_list{head};
        vector<Node*> random_pointer_list{head->random};
        while (node->next != nullptr) {
            node = node->next;
            Node* next_node = new Node(node->val);
            new_node->next = next_node;
            new_node = new_node->next;
            new_node_list.push_back(new_node);
            node_list.push_back(node);
            random_pointer_list.push_back(node->random);
        }
        new_node = ans;
        for (auto node:random_pointer_list) {
            if (node == nullptr) {
                new_node->random = nullptr;
                new_node = new_node->next;
            }
            else {
                for (int i = 0; i < node_list.size(); ++i){
                    if (node_list[i] == node) {
                        new_node->random = new_node_list[i];
                        new_node = new_node->next;
                        break;
                    }
                }
            }
        }

        return ans;

    }
};

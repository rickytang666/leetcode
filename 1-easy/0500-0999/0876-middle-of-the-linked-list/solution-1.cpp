#include <bits/stdc++.h>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* middleNode(ListNode* head) {

        vector<ListNode*> nodes;

        while (head != nullptr) {
            nodes.push_back(head);
            head = head->next;
        }

        return nodes.at(nodes.size() / 2);
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}
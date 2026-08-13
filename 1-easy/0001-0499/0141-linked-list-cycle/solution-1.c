#include <stdbool.h>

// Definition for singly-linked list.
struct ListNode
{
    int val;
    struct ListNode *next;
};

bool helper(struct ListNode *slow, struct ListNode *fast)
{
    if (!slow || !fast || !fast->next)
        return false;
    slow = slow->next;
    fast = fast->next->next;
    if (slow == fast)
        return true;
    return helper(slow, fast);
}

bool hasCycle(struct ListNode *head)
{
    return helper(head, head);
}
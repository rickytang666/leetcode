#include <stdlib.h>

/**
 * Definition for singly-linked list.
 */
struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *deleteDuplicates(struct ListNode *head)
{
    struct ListNode dummy;
    dummy.val = -101;
    dummy.next = head;

    struct ListNode *prev = &dummy;
    struct ListNode *curr = head;

    while (curr)
    {
        if (curr->next && curr->val == curr->next->val)
        {
            int v = curr->val;
            while (curr && curr->val == v)
            {
                curr = curr->next;
            }
            prev->next = curr;
        }
        else
        {
            prev = curr;
            curr = curr->next;
        }
    }

    return dummy.next;
}
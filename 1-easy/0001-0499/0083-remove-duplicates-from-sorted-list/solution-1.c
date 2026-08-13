#include <stdlib.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *deleteDuplicates(struct ListNode *head)
{
    struct ListNode *current = head;

    while (current && current->next)
    {
        while (current->next && current->val == current->next->val)
        {
            current->next = current->next->next;
        }

        current = current->next;
    }

    return head;
}
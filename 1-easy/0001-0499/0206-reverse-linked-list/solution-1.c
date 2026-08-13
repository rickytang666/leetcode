#include <stdlib.h>

// Definition for singly-linked list.
struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *reverseList(struct ListNode *head)
{
    if (!head)
        return NULL;
    if (!head->next)
        return head;

    struct ListNode *prev = NULL;
    struct ListNode *curr = head;

    while (curr)
    {
        struct ListNode *nx = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nx;
    }

    return prev;
}
#include <stdlib.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB)
{
    if (!headA || !headB)
        return NULL;

    struct ListNode *curr1 = headA;
    struct ListNode *curr2 = headB;

    while (curr1 != curr2)
    {
        curr1 = curr1 ? curr1->next : headB;
        curr2 = curr2 ? curr2->next : headA;
    }

    return curr1;
}
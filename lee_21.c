#include <stddef.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;
};

typedef struct ListNode ListNode;


struct ListNode *mergeTwoLists(struct ListNode *l1, struct ListNode *l2)
{
    if (l1 == NULL && l2 == NULL) {
        return NULL;
    }
    ListNode *merge = malloc(sizeof(ListNode));
    ListNode *p = merge;
    while (l1 != NULL && l2 != NULL) {
        if (l1->val > l2->val) {
            p->next = l2;
            l2 = l2->next;
        } else {
            p->next = l1;
            l1 = l1->next;
        }
        p = p->next;
    }
    if (l1 != NULL) {
        p->next = l1;
    }
    if (l2 != NULL) {
        p->next = l2;
    }
    return merge->next;
}

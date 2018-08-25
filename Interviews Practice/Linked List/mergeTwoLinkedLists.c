// Definition for singly-linked list:
// typedef struct list_##name {
//   type value;
//   struct list_##name *next;
// } list_##name;
//
// list_##name *alloc_list_##name(type v) {
//   list_##name *l = calloc(1, sizeof(list_##name));
//   l->value = v;
//   return l;
// }
//
list_integer * mergeTwoLinkedLists(list_integer * l1, list_integer * l2) {
    if(l1 == NULL)
        return l2;
    else if(l2 == NULL)
        return l1;
    
    list_integer *node;
    if(l1->value <= l2->value) 
    {
        node = l1;
        node->next = mergeTwoLinkedLists(l1->next, l2);
        return node;
    }
    else
    {
        node = l2;
        node->next = mergeTwoLinkedLists(l1, l2->next);
        return node;
    }
}

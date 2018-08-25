# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    head = l
    tail = l
    while(n != 0):
        head = head.next
        n -= 1
    
    if head == None or head == l:
        return l
    while(head.next != None):
        tail = tail.next
        head = head.next
    
    
    list_head = tail.next
    list_tail = head
    tail.next = None
    list_tail.next = l
    return list_head
    
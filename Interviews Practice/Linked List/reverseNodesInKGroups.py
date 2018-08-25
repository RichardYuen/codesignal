# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    cnt = 0
    curr = l
    while(curr != None and cnt < k):
        curr = curr.next
        cnt += 1
    
    if cnt < k:
        return l
    
    prev = None
    curr = l
    next = None
    while(cnt != 0 and curr != None):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        cnt -= 1
    
    if next is not None:
        l.next = reverseNodesInKGroups(next, k)
    
    return prev
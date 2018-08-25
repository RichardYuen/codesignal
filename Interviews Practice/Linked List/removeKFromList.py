# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def removeKFromList(l, k):
    prev = None
    curr = l
    
    while(curr != None):
        if(curr.value == k):
            if(prev == None):
                l = curr.next
            else:
                prev.next = curr.next
        else:
            prev = curr
        
        curr = curr.next
    
    return l

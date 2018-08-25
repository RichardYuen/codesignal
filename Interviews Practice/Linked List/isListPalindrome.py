# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseList(l):
    prev = None
    next = None
    curr = l
    while(curr != None):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next        
    
    l = prev
    return l

def compareList(l1, l2):
    temp1 = l1
    temp2 = l2
    while(temp1 != None and temp2 != None):
        if(temp1.value == temp2.value):
            temp1 = temp1.next
            temp2 = temp2.next
        else:
            return False
        
    return True

def isListPalindrome(l):
    slow_ptr = l
    fast_ptr = l
    while(fast_ptr != None and fast_ptr.next !=None):
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
    
    if(fast_ptr != None):
        slow_ptr = slow_ptr.next
        
    half = slow_ptr
    half = reverseList(half)
    
    return compareList(l, half)
    
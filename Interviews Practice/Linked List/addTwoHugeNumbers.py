# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    stack1 = []
    stack2 = []
    temp = a
    while(temp != None):
        stack1.append(temp.value)
        temp = temp.next
        
    temp = b
    while(temp != None):
        stack2.append(temp.value)
        temp = temp.next
        
    rem = 0
    next = None
    while(len(stack1) != 0 and len(stack2) != 0):
        num1 = stack1.pop()
        num2 = stack2.pop()
        node = ListNode((num1 + num2 + rem) % 10000)
        rem = (num1 + num2 + rem) // 10000
        node.next = next
        next = node
    
    while(len(stack1) != 0):
        num1 = stack1.pop()
        node  = ListNode((num1 + rem) % 10000)
        rem = (num1 + rem) // 10000
        node.next = next
        next = node
        
    while(len(stack2) != 0):
        num2 = stack2.pop()
        node  = ListNode((num2 + rem) % 10000)
        rem = (num2 + rem) // 10000
        node.next = next
        next = node        
    
    if rem != 0:
        node = ListNode(rem)
        node.next = next
        next = node
        
    return node
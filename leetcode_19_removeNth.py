"""Remove the Nth element from the linkedlist slow fast pointer"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""To do this in one pass, has two pointers to point in the linked list structure"""

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None or head.next == None:
            return None
        #two pointers, one front, one back
        back = head
        front = back
        for i in range(n+1):
            #check condtions when front is already None before N; linkedlist  < n
            if front == None:
                return head.next
            front = front.next
        while front is not None:
            back = back.next
            front = front.next
        back.next = back.next.next
        return head
    
    
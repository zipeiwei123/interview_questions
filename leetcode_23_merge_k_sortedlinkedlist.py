"""This question is combined heap and linkedlist. 
    Through every linked list in min_heap
    heapify min heap
    throw it back to the list node
    """
#use libray
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        #append all the linked list that has value
        for linked_list in lists:
            head = linked_list
            while head:
                heap.append(head.val)
                head = head.next
        if heap:
            #sort the heap
            heap.sort()
            #get new linked_list
            new_linked_list = self.send_back_to_linked_list(heap)
            return new_linked_list
        else:
            return None
        
"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while (lists.count(None)):
            lists.remove(None)
        o_list = ListNode()
        pointer = o_list
        while lists: 
            minimum = self.find_min(lists)
            pointer.next = ListNode(val=minimum)
            pointer = pointer.next
            counter = 0
            while lists[counter].val != minimum:
                counter += 1
            if lists[counter].next is None:
                del lists[counter]
            else:
                lists[counter] = lists[counter].next
        return o_list.next

    def find_min(self, lists):
        min = lists[0].val
        for lst in lists[1:]:
            if lst.val < min:
                min = lst.val
        return min

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#use fast and slow pointers to get the 2 halves of the list
# a lot of pointers, a lot of edge cases

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        slow.next = None # splitting the list into 2 different lists
        prev = None
        
        #reversing second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        #merge two lists
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
            
            
        

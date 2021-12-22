# Problem: https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        #find middle
        
        if not head:
            return []
        
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse second half
        prev, curr = None, slow.next
        
        while curr:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        slow.next = None
        
        #merge first half and second half
        first_half = head
        second_half = prev
        
        while second_half:
            first_half_next = first_half.next
            first_half.next = second_half
            first_half = second_half
            second_half = first_half_next

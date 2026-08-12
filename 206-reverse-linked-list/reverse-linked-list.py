# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # if not root:
        #     return root
        
        t1 = head
        prev = None
        while t1 != None:
            temp = t1.next
            t1.next = prev
            prev = t1
            t1 = temp 
        
        return prev

        
        
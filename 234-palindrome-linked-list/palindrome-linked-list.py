# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        t1 = head
        slow = t1
        fast = t1
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        t1 = slow
        prev = None
        while t1 != None:
            temp = t1.next
            t1.next = prev
            prev = t1
            t1 = temp
        t1 = head
        while prev != None:
            if t1.val != prev.val:
                return False
            t1 = t1.next
            prev = prev.next
        return True

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
        
        if head == None or head.next == None:
            return True

        # Find middle
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        def rev(head1):
            prev = None
            t2 = head1

            while t2 != None:
                temp = t2.next
                t2.next = prev
                prev = t2
                t2 = temp

            return prev

        head1 = rev(slow)

        # Compare first half and reversed second half
        t1 = head
        t2 = head1

        while t2 != None:
            if t1.val != t2.val:
                return False

            t1 = t1.next
            t2 = t2.next

        return True
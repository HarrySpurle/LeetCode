class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''
        curr = l1
        while curr:
            num1 = str(curr.val) + num1
            curr = curr.next
        curr = l2
        while curr:
            num2 = str(curr.val) + num2
            curr = curr.next
        total = str(int(num1) + int(num2))
        dummy = ListNode()
        curr = dummy
        for digit in reversed(total):
            curr.next = ListNode(int(digit))
            curr = curr.next
        return dummy.next
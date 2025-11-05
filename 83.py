class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while (current and current.next):
            if (current.val == current.next.val):
                current.next = current.next.next
                continue
            current = current.next
        return head
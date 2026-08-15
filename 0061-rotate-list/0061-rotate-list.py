class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        n = 1
        last = head
        while last.next != None:
            n += 1
            last = last.next
        k = k % n
        if k == 0:
            return head
        t = head
        count = 1
        while count < n - k:
            t = t.next
            count += 1
        new_head = t.next
        t.next = None
        last.next = head
        return new_head
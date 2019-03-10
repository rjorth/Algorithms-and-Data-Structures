def deleteDuplicates(self, head: ListNode) -> ListNode:
        tracker = head 
        while tracker:
            while tracker.next and tracker.val == tracker.next.val:
                tracker.next = tracker.next.next
            tracker = tracker.next
        return head

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        current = head

        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Main program
if __name__ == "__main__":
    # Create the sorted linked list: 1 -> 1 -> 2
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)

    solution = Solution()
    new_head = solution.deleteDuplicates(head)
    print_linked_list(new_head)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()  # Dummy node to start the merged list
        current = dummy  # Pointer to traverse the merged list
    
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append remaining nodes from list1 or list2
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return dummy.next  # Return the merged list starting from the next of the dummy node

    
solution = Solution()
# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("Finish!")

# Main program
if __name__ == "__main__":
    # Input for list1
    list1_values = list(map(int, input("Enter space-separated values for list1: ").split()))
    list1 = create_linked_list(list1_values)

    # Input for list2
    list2_values = list(map(int, input("Enter space-separated values for list2: ").split()))
    list2 = create_linked_list(list2_values)

    # Merge lists
    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)

    # Print the merged list
    print("Merged List:")
    print_linked_list(merged_list)




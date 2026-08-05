class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


# create linked list
def create_list(arr):
    head = ListNode(arr[0])
    temp = head

    for i in arr[1:]:
        temp.next = ListNode(i)
        temp = temp.next

    return head


# print linked list
def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()



arr = list(map(int, input().split()))

head = create_list(arr)

print("Original:")
print_list(head)

sol = Solution()
head = sol.reverseList(head)

print("Reversed:")
print_list(head)
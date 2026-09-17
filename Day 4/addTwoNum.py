class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

def create_list(arr):
    head = ListNode(arr[0])
    temp = head

    for i in arr[1:]:
        temp.next = ListNode(i)
        temp = temp.next

    return head


def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

l1_arr = list(map(int, input().split()))
l2_arr = list(map(int, input().split()))

l1 = create_list(l1_arr)
l2 = create_list(l2_arr)

sol = Solution()
result = sol.addTwoNumbers(l1, l2)

print("Result:")
print_list(result)
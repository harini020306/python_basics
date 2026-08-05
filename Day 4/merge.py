class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next


# ---------- helper functions ----------

def create_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    temp = head

    for val in arr[1:]:
        temp.next = ListNode(val)
        temp = temp.next

    return head


def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


# ---------- input section ----------

print("Enter first sorted list:")
l1 = list(map(int, input().split()))

print("Enter second sorted list:")
l2 = list(map(int, input().split()))

list1 = create_list(l1)
list2 = create_list(l2)

# ---------- run ----------

sol = Solution()
result = sol.mergeTwoLists(list1, list2)

print("Merged List:")
print_list(result)
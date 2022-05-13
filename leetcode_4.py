### Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  
    ### solution 1
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        al = []
        while list1:
            al.append(list1.val)
            list1 = list1.next
        while list2:
            al.append(list2.val)
            list2 = list2.next
        al.sort()
        res = ListNode(0)
        rr = res
        for i in al:
            rr.next = ListNode(i)
            rr = rr.next
        return res.next
    
    ### solution 2
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        rres = res
        while list1 and list2:
            if list1.val < list2.val:
                rres.next = list1
                rres = rres.next
                list1 = list1.next
            else:
                rres.next = list2
                rres = rres.next
                list2 = list2.next
        rres.next = list1 or list2
        return res.next

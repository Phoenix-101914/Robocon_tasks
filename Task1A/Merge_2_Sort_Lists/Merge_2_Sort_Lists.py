# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        list3=ListNode()
        node=list3

        while list1 is not None and list2 is not None:
            if list1.val<list2.val:
                node.next=list1
                list1=list1.next
            else:
                node.next=list2
                list2=list2.next
            node=node.next
        if list2 is None and list1 is not None:
            while list1 is not None:
                node.next=list1
                list1=list1.next
                node=node.next
        if list1 is None and list2 is not None:
            while list2 is not None:
                node.next=list2
                list2=list2.next
                node=node.next

        return list3.next
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
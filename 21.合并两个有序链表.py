#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        yaml = ListNode(-1)
        merge = yaml
        point1 = l1
        point2 = l2
        while point1 and point2:
            if point1.val < point2.val:
                merge.next = point1
                point1 = point1.next
            else:
                merge.next = point2
                point2 = point2.next
            merge = merge.next
        if point1:
            merge.next = point1
        if point2:
            merge.next = point2
        return yaml.next 



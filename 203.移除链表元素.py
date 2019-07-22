#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# https://leetcode-cn.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (41.84%)
# Likes:    261
# Dislikes: 0
# Total Accepted:    30.8K
# Total Submissions: 73.7K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 删除链表中等于给定值 val 的所有节点。
# 
# 示例:
# 
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(None)
        dummy.next = head
        preNode = dummy
        node = head
        while node:
            if node.val == val:
                preNode.next = node.next
                node = node.next
            else:
                preNode = node
                node = node.next
        return dummy.next


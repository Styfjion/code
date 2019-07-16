#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (62.75%)
# Likes:    483
# Dislikes: 0
# Total Accepted:    72.4K
# Total Submissions: 115.4K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#递归法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead
#循环法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        node = head
        preNode = None
        while node:
            temp = node.next
            node.next = preNode
            preNode = node
            node = temp
        return preNode






        

            
        


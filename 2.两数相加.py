#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (35.72%)
# Likes:    3162
# Dislikes: 0
# Total Accepted:    221.5K
# Total Submissions: 619.9K
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
# 示例：
# 
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
方法一
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return 0
        a = 0
        b = 0
        mi = 1
        while l1 or l2:
            if l1:
                a += mi*l1.val
                l1 = l1.next
            if l2:
                b += mi*l2.val
                l2 = l2.next
            mi *= 10
        res_str = str(a+b)[::-1]
        root = ListNode(res_str[0])
        node = root
        for i in range(1,len(res_str)):
            temp = ListNode(res_str[i])
            node.next = temp
            node = temp
        return root
"""


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return
        elif not l1:
            return l2
        elif not l2:
            return l1
        a = l1.val + l2.val
        node = ListNode(a%10)
        node.next = self.addTwoNumbers(l1.next,l2.next)
        if a>=10:
            node.next = self.addTwoNumbers(node.next,ListNode(1))
        return node

# @lc code=end


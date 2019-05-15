class ListNode:
    def __init__(self,x=None):
        self.value = x
        self.Next = None
class Solution:
    def DeleteOneListNode(self,firstNode,deleteNode):
        if not firstNode or not deleteNode:
            return
        if deleteNode.Next:
            nextNode = deleteNode.Next
            deleteNode.value = nextNode.value
            deleteNode.Next = nextNode.Next
            nextNode = None
        elif firstNode == deleteNode:
            firstNode = None
            deleteNode = None
        else:
            indexNode = firstNode
            while indexNode.Next!=deleteNode:
                indexNode = indexNode.Next
            indexNode.Next = None
            deleteNode = None

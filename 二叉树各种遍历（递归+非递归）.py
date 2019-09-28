#输入：
###          A
#        /        \
#     B            C
#   /  \          /  \
#  D     E      F     G
#       /        \
#      H           I
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

#前序递归
def preOrder_1(node):
    if not node:
        return 
    print(node.val, end =" ")
    preOrder_1(node.left)
    preOrder_1(node.right)

#前序非递归
def preOrder_2(node):
    if not node:
        return
    stack = [node]
    while stack:
        top = stack.pop()
        print(top.val,end =" ")
        if top.right:
            stack.append(top.right)
        if top.left:
            stack.append(top.left)

#中序递归
def inOrder_1(node):
    if not node:
        return
    inOrder_1(node.left)
    print(node.val,end =" ")
    inOrder_1(node.right)

#中序非递归
def inOrder_2(node):
    if not node:
        return
    point = node
    stack = []
    while point or stack:
        if point:
            stack.append(point)
            point = point.left
        else:
            point = stack.pop()
            print(point.val,end =" ")
            point = point.right

#后序递归
def postOrder_1(node):
    if not node:
        return
    postOrder_1(node.left)
    postOrder_1(node.right)
    print(node.val,end =" ")

#后序非递归
def postOrder_2(node):
    if not node:
        return
    stack = [node]
    stack2 = []
    while stack:
        top = stack.pop()
        stack2.append(top)
        if top.left:
            stack.append(top.left)
        if top.right:
            stack.append(top.right)
    while stack2:
        print(stack2.pop().val,end =" ")

#按层次遍历
def layerOrder(node):
    if not node:
        return
    queue = [node]
    while queue:
        top = queue.pop(0)
        print(top.val)
        if top.left:
            queue.append(top.left)
        if top.right:
            queue.append(top.right)

#二叉树节点个数
def treeNumber(node):
    if not node:
        return 0
    nums = treeNumber(node.left)+treeNumber(node.right)
    return nums+1

#二叉树深度
def treeDepth(node):
    if not node:
        return 0
    nums = max(treeDepth(node.left),treeDepth(node.right))
    return nums+1

if __name__ == "__main__":
    chars = [TreeNode(chr(i)) for i in range(ord('A'),ord('I')+1)]
    a,b,c,d,e,f,g,h,i = chars
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    e.left = h
    f.right = i
    preOrder_1(a)
    print("-----------------------------------------")
    preOrder_2(a)
    print("-----------------------------------------")
    inOrder_1(a)
    print("-----------------------------------------")
    inOrder_2(a)
    print("-----------------------------------------")
    postOrder_1(a)
    print("-----------------------------------------")
    postOrder_2(a)
    print("-----------------------------------------")
    print(treeNumber(a))
    print("-----------------------------------------")
    print(treeDepth(a))



"""
结果:
A B D E H C F I G -----------------------------------------
A B D E H C F I G -----------------------------------------
D B H E A F I C G -----------------------------------------
D B H E A F I C G -----------------------------------------
D H E B I F G C A -----------------------------------------
D H E B I F G C A -----------------------------------------
9
-----------------------------------------
4
"""
    



        
        



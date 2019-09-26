#输入：
###          A
#        /        \
#     B            C
#   /  \          /  \
#  D     E      F     G
#       /        \
#      H           I
#输出：     
# LayerOrder: 
# A 
# BC 
# DEFG 

class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None


def bfs(root):  # 传入树的根节点
    q = [root]
    result = []
    while q:
        every_layer = []
        length = len(q)
        for i in range(length):
            r = q.pop(0)
            if r.left:
               q.append(r.left)
            if r.right:
               q.append(r.right)
            every_layer.append(r.val)
        result.append(every_layer)
    return result

if __name__ == "__main__":
    a = TreeNode('A')
    b = TreeNode('B')
    c = TreeNode('C')
    d = TreeNode('D')
    a.left = b
    a.right = c
    b.left = d
    print(bfs(a))
    
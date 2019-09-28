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

def dfs(root):
    if not root:
        return
    stack = [root]
    res = []
    while stack:
        top = stack.pop()
        res.append(top.val)
        if top.right:
            stack.append(top.right)
        if top.left:
            stack.append(top.left)
    return res

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
    print(dfs(a))






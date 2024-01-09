class TreeNode():
    def  __init__(self,
                  val   = None,
                  left  = None,
                  right = None):
        self.val        = val
        self.left  = left
        self.right = right

def insert(root: TreeNode, val: int) -> TreeNode:
    if root is None:
        return TreeNode(val, None, None)
    if val > root.val:
        root.right = insert(root.right, val)
    else:
        root.left = insert(root.left, val)
    return root

def search(root: TreeNode, val: int) -> TreeNode:
    if root == None:
        return None
    if root.val == val:
        return root
    if val < root.val:
        aa = search(root.left, val)
        return aa
    else:
        bb = search(root.right, val)
        return bb

def delete(root: TreeNode, key: int) -> TreeNode:
    if root == None:
        return None
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if root.left == None and root.right == None:
            return None
        if root.left != None and root.right == None:
            return root.left
        if root.right != None and root.left == None:
            return root.right

        t = root.right
        while(t.left != None):
            t = t.left
        root.val = t.val
        root.right = delete(root.right, t.val)

    return root

def preorderTraversal(root: TreeNode):
        arr = []
        if root == None:
            return root
        arr.append(root.val)
        if root.left != None:
            arr.extend(preorderTraversal(root.left))
        if root.right != None:
            arr.extend(preorderTraversal(root.right)) 
          
        return arr

def postorderTraversal( root:TreeNode):
        arr = []
        if root == None:
            return root
        if root.left != None:
            arr.extend(postorderTraversal(root.left))
        if root.right != None:
            arr.extend(postorderTraversal(root.right)) 
        arr.append(root.val)  
        return arr

def inorderTraversal(root: TreeNode):
        arr = []
        if root == None:
            return root
        
        if root.left != None:
            arr.extend(inorderTraversal(root.left))
        arr.append(root.val)
        if root.right != None:
            arr.extend(inorderTraversal(root.right)) 
          
        return arr


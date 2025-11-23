# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree  85%
# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/description

#Input: tree = [7,4,3,null,null,6,19], target = 3
#Output: 3

class Tree:
    def __init__(self, n):
        if self.head is None:
            self.head = n
            return self

    def create_tree(self, n):
        current_node = n
        if current_node.left is None:
            current_node.left = n
        elif current_node.right is None:
            current_node.right = n

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def getTargetCopy(self, original, cloned, target):
        clone_treenode_list = [cloned]

        while clone_treenode_list:
            currentFromClone = clone_treenode_list.pop(0)

            if currentFromClone.val == target.val:
                return currentFromClone

            if currentFromClone.left:
                clone_treenode_list.append(currentFromClone.left)

            if currentFromClone.right:
                clone_treenode_list.append(currentFromClone.right)


####################################
# Just for us for testing
####################################
from collections import deque

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert_breadth_first(self, value):
        new_node = TreeNode(value)
        queue = deque([self.root])

        while queue:
            current = queue.popleft()

            # Check left child
            if current.left is None:
                current.left = new_node # type: ignore
                return
            else:
                queue.append(current.left)

            # Check right child
            if current.right is None:
                current.right = new_node # type: ignore
                return
            else:
                queue.append(current.right)

    def print_tree(self):
        clone_treenode_list = [self.root]

        while clone_treenode_list:
            currentFromClone = clone_treenode_list.pop(0)
            print(currentFromClone.val)

            if currentFromClone.left:
                clone_treenode_list.append(currentFromClone.left)
            if currentFromClone.right:
                clone_treenode_list.append(currentFromClone.right)

########
# local testing
########
def find_node_bfs(clonedRoot, targetFromOriginal):
    clone_treenode_list = [clonedRoot]

    while clone_treenode_list:
        currentFromClone = clone_treenode_list.pop(0)

        if currentFromClone.val == targetFromOriginal.val:
            return currentFromClone.val

        if currentFromClone.left:
            clone_treenode_list.append(currentFromClone.left)

        if currentFromClone.right:
            clone_treenode_list.append(currentFromClone.right)

## arr = [4,3,None,None,6,19]

arr = [None,6,None,5,None,4,None,3,None,2,None,1]

test_tree = BinaryTree(8)
for val in arr:
    test_tree.insert_breadth_first(val)

# test_tree.print_tree()
target_tree_node = TreeNode(4)

print (find_node_bfs(test_tree.root, target_tree_node))

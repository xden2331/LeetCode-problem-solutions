# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        isLTR = True
        current_level = [root]

        while current_level:
            current_level_val = []
            next_level = []
            for node in current_level:
                if node != None:
                    current_level_val.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
            if current_level_val:
                if isLTR == False:
                    current_level_val.reverse()
                levels.append(current_level_val)
            current_level = next_level
            isLTR = False if isLTR else True

        return levels
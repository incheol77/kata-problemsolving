
# using BFS
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        next_level = deque([root])
        while root and next_level:
            curr_level = next_level
            next_level = deque()
            levels.append([])
            for node in curr_level:
                levels[-1].append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        return levels[::-1]

# using DFS
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)

            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)

        helper(root, 0)
        return levels[::-1]

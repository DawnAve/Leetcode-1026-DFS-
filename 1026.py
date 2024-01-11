# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def getMax(root, maxx,minn):

            # Base case for recursion
            if not root:
                return 0

            # A maximized difference needs a maximized Max and a minimized Min
            maxx = max(maxx, root.val)
            minn = min(minn, root.val)

            # Since left and right can't share the same Min, we use a temp to hold the Min from the parent
            # because Min will probably be changed when going through the left branch
            temp = minn
            
            diff = maxx - minn
            diff = max(diff, getMax(root.left, maxx, minn))

            # Reset Min  (If you don't, you can also use "temp" as "minn" in the next line)
            minn = temp
            diff = max(diff, getMax(root.right, maxx, minn))
            return diff
        return getMax(root, root.val, root.val)
        

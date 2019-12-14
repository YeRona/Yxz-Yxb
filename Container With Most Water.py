'''
Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints 
of line i is at (i, ai) and (i, 0). Find two lines, which 
together with x-axis forms a container, such that 
the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        s = 0
        if height[0] > height[n - 1]:
            height = height[::-1]
        for i in range(n):
            s = max(s, (n - 1 - i) * min(height[n-1], height[i]))
            if height[i] <= height[n-1]:
                pass
            else:
                right = height[n - 1]
                for j in range(n - 2, i, -1):
                    if height[j] > right:
                        mi = min(height[j], height[i])
                        right = height[j]
                        if ((j - i) * mi > s):
                            s = (j - i) * mi
                        if height[i] <= right:
                            break
        return s
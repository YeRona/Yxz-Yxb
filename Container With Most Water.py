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
        j = n - 1
        i = 0
        while i < j:
            if height[i] < height[j]:
                s = max(s, (j - i) * height[i])
                i += 1
            else:
                s = max(s, (j - i) * height[j])
                j -= 1
        return s

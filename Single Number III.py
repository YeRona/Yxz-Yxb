'''
Given an array of numbers nums, in which 
exactly two elements appear only once and 
all the other elements appear exactly twice. 
Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        t = []
        h = {}
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                h[i] = 2
        for i in h:
            if h[i] == 1:
                t.append(i)
        return t
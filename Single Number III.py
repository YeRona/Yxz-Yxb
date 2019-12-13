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
        re = set()
        remo = set()

        for i in nums:
            if i not in remo:
                remo.add(i)
            else:
                re.add(i)
        return remo - re

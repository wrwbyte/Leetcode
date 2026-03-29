#Problem 1
#Solved in 0ms
#https://leetcode.com/problems/two-sum/

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Approach: For each index find its pair (target-num)
#Check if this has been seen in the list so far (Dictionary)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        passed = {} #Track the index of past numbers
        for i, val in enumerate(nums):
            pair = target - val
            if pair in passed:
                return [passed[pair],i]
            passed[val] = i

        
#Problem 4
#Solved in 15ms
#https://leetcode.com/problems/median-of-two-sorted-arrays/

#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

#Approach: Check if both arrays exist, combine them into 1 array and find the median
#O(m+n) rather than the binary O(log(m+n))

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        while nums1 or nums2:
            if not nums1:
                nums3.append(nums2[0])
                nums2.pop(0) 
            elif not nums2:
                nums3.append(nums1[0])
                nums1.pop(0) 
            elif nums1[0] > nums2[0]:
                nums3.append(nums2[0])
                nums2.pop(0)
            else: #handle 2>1 and ties
                nums3.append(nums1[0])
                nums1.pop(0)
        if len(nums3)%2 == 0:
            half = len(nums3)//2
            return (nums3[half-1]+nums3[half])/2.0
        else:
            half = (len(nums3)//2)
            return nums3[half]

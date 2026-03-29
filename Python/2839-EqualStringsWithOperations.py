#Problem 2839
#Solved in 3ms
#https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/?envType=daily-question&envId=2026-03-29

#You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.
#You can apply the following operation on any of the two strings any number of times:
#   Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.
#Return true if you can make the strings s1 and s2 equal, and false otherwise.

#Approach: treat total possibilites like 2 bits (00,01,10,11)
#Brute force check each one
class Solution(object):
    def swap(self, s1, index1, index2):
        """
        :type s1: str
        :type index1: int
        :type index2: int
        :rtype: str
        """
        # convert string to list
        s_list = list(s1)
        # swap positions
        s_list[index1], s_list[index2] = s_list[index2], s_list[index1]
        # convert back to string
        return "".join(s_list)


    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #Total indices combinations: 0/2, 1/3, both, none 
        #Two bits
        if (s1 == s2):    #00
            return True

        s1 = self.swap(s1,0,2) 
        if (s1 == s2):    #10
            return True

        s1 = self.swap(s1,0,2)
        s1 = self.swap(s1,1,3)
        if (s1 == s2):    #01
            return True

        s1 = self.swap(s1,0,2)
        if (s1 == s2):    #11
            return True
        return False



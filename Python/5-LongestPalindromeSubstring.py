#Problem 5
#Solved in 3866ms
#https://leetcode.com/problems/longest-palindromic-substring/

#Given a string s, return the longest palindromic substring in s.

#Approach: Divide the string into its longest substrings and check each one untill you get to one char

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        for leng in range(len(s), 0, -1):  # start from longest
            for start in range(len(s) - leng + 1):
                substring = s[start:start+leng]
                if substring == substring[::-1]:
                    return substring  # first palindrome of this length is the longest
                

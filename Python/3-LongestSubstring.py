#Problem 3
#Solved in 13ms
#https://leetcode.com/problems/longest-substring-without-repeating-characters/

#Given a string s, find the length of the longest substring without duplicate characters.

#Approach:
#Naviagte through the string and track substring length
#When I encounter a duplicate, pop from string untill the repeat character is gone

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length, temp = 0,0
        current = []
        #Corner Cases when "" or " "
        if not s:
            return 0
        if s.isspace():
            return 1


        for letters in s:
            if letters in current:
                if length < temp:
                    length = temp
                current.append(letters)

                while current[0] != letters: #Pop untill there are only unique chars 
                    current.pop(0)
                current.pop(0)

                temp = len(current) #Fix length after cutting letters
            else:
                current.append(letters) #Track new unique letter
                temp = temp + 1
        if length < temp: #Incase substring is at the end of the string
                    length = temp
        return length
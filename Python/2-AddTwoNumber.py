#Problem 2
#Solved in 7ms
#https://leetcode.com/problems/add-two-numbers/

#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.


#Approach: Add each node together and track carry over

#Definition for singly-linked list.
#class ListNode(object):
 #   def __init__(self, val=0, next=None):
  #      self.val = val
   #     self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        sol = head
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sol.val = (val1 + val2 + carry)%10 #Modular for if sum > 9
            carry = (val1 + val2 + carry)//10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2 or carry:
                sol.next = ListNode()
                sol = sol.next 
            
        return head


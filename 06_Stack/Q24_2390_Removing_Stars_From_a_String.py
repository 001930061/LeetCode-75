'''
2390. Removing Stars From a String

You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters and stars *.
The operation above can be performed on s.
'''
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str  # 输入的字符串
        :rtype: str  # 返回处理后的字符串
        """

        stack = []  # 初始化一个栈，用于存储字符

        # 遍历输入字符串中的每个字符
        for char in s:
            if char == '*':
                # 如果当前字符是星号('*')，则从栈中弹出最后一个字符
                if stack:  # 确保栈不为空
                    stack.pop()
            else:
                # 如果当前字符不是星号，则将其推入栈中
                stack.append(char)
        
        # 将栈中的字符合并成字符串并返回
        return ''.join(stack)
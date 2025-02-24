'''
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
'''

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack_letters = []  # 用于存储之前的字符串
        stack_nums = []     # 用于存储数字
        current_string = '' # 当前构建的字符串
        current_number = 0  # 当前构建的数字

        for char in s:
            if char.isdigit():  # 如果字符是数字
                current_number = current_number * 10 + int(char)  # 处理多位数字
            elif char == '[':  # 如果字符是左括号
                # 将当前数字和字符串推入栈中
                stack_nums.append(current_number)
                stack_letters.append(current_string)
                current_string = ''  # 重置当前字符串
                current_number = 0   # 重置当前数字
            elif char == ']':  # 如果字符是右括号
                # 弹出栈中的数字和字符串
                previous_number = stack_nums.pop()
                previous_string = stack_letters.pop()
                # 构建当前字符串，将之前的字符串和当前字符串重复 previous_number 次
                current_string = previous_string + current_string * previous_number
            
            else:  # 如果是普通字符
                current_string += char  # 追加字符到当前字符串
        
        return current_string  # 返回最终构建的字符串
'''
151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. 
Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space 
in the reversed string.
'''

'''
这题很简单, 先把数据预处理一下, 用空格当界限打散, 然后放入stack, 再后再把stack顺序倒过来拼起来就行
'''

# ---------------- Final Answer: Time Complexity = O(n), Space Complexity = O(n)---------------- #

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 先把string拆散
        string = s.split()

        # 把每个单词加到stack里面
        stack = [word for word in string]
        
        # 把stack的顺序颠倒
        stack.reverse()

        # 把stack 用空格拼起来，返回
        return ' '.join(stack)
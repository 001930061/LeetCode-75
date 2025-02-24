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
        :type s: str  # 输入的字符串，包含一个或多个单词
        :rtype: str   # 返回反转单词顺序后的字符串
        """
        # 先把字符串拆分成单词，使用空格作为分隔符
        string = s.split()

        # 将每个单词添加到栈中
        stack = [word for word in string]
        
        # 将栈中的单词顺序颠倒
        stack.reverse()

        # 将栈中的单词用空格拼接起来，返回反转后的字符串
        return ' '.join(stack)
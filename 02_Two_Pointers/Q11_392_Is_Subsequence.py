'''
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, 
and you want to check one by one to see if t has its subsequence. In this scenario, 
how would you change your code?

'''

'''
对于这一题 我们需要两个指针 
一个指针用于从s中读取char
另一个指针用于从t中找匹配

只能遍历一次list 这样才能保证s中的顺序不会影响结果
'''


# ————————————————————————————————————————————————————————————————————

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str  # 输入的字符串s
        :type t: str  # 输入的字符串t
        :rtype: bool  # 返回值为布尔值，表示s是否为t的子序列
        """

        # 这里初始化从s中读取的指针
        reader = 0
        # 获取s和t的长度方便作对比
        length_s = len(s)
        length_t = len(t)

        # 由于空字符串是所有字符串的子字符串，所以直接返回True
        if length_s == 0:
            return True

        # 遍历t字符串
        for checker in range(length_t):
            # 如果找到匹配的字符
            if t[checker] == s[reader]:
                # reader的指针向后移动一位
                reader += 1

                # 如果s中的最后一个字符都匹配完成了, 那么直接返回True
                if reader == length_s:
                    return True
        
        # s中还有元素没能匹配，返回False
        return False
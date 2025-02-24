'''
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
'''

'''
还是滑动窗口
这次不是算平均数
而是计算里面有的元音的个数
'''

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str  # 输入的字符串
        :type k: int  # 子串的长度
        :rtype: int  # 返回最大元音字母的数量
        """
        # 定义元音字母的集合
        vowels = {'a', 'e', 'i', 'o', 'u'}

        max_vowels = 0  # 初始化最大元音数量
        count = 0  # 初始化当前窗口中的元音数量

        # 计算第一个长度为k的子串中的元音数量
        for i in range(k):
            if s[i] in vowels:
                count += 1
            
        max_vowels = count  # 更新最大元音数量

        # 从索引k开始，滑动窗口
        for i in range(k, len(s)):
            # 如果窗口的最左边字符是元音，减少计数
            if s[i - k] in vowels:
                count -= 1
            # 如果新进入窗口的字符是元音，增加计数
            if s[i] in vowels:
                count += 1
            # 更新最大元音数量
            max_vowels = max(max_vowels, count)

        return max_vowels  # 返回最大元音数量


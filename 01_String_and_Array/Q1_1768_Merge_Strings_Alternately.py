'''
1768. Merge Strings Alternately
You are given two strings word1 and word2. Merge the strings by 
adding letters in alternating order, starting with word1. If a 
string is longer than the other, append the additional letters 
onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
'''


'''
首先，我们来分析问题：

对于 word1 和 word2 两个字符串，我们需要将它们的字母依次交替拼接在一起（如果其中一个字符串为空，该怎么办？）。

为了解决这个问题，我们可以定义两个指针来辅助读取字符串，并考虑字符串长度不同的情况，可能导致某个指针先到达字符串末尾。

在 while 循环终止后，需要分别处理以下两种情况：
	1.	index_a 先到达字符串末尾
	2.	index_b 先到达字符串末尾

无论哪种情况发生，都需要将未遍历完的字符串部分添加到结果中，最终返回拼接后的结果。

边界情况：
	•	如果某个字符串为空，或者两个字符串都为空，那么 while 语句不会执行，直接进入后续处理。
	•	如果两个字符串都为空，则最终返回的 result 也是空字符串。
'''

# ---------------- Final Answer: Time Complexity = O(n), Space Complexity = O(n)---------------- #

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # 分别为两个string定义指针, 用于读取char
        index_a, index_b = 0, 0

        # 定义一个列表用于存储收集到的chars
        result = []

        # 定义两个integers来表示两个字符串的长度
        lens_1, lens_2 = len(word1), len(word2)

        # 依次分别冲两个string里面按顺序取char, 指导某一个指针到达字符串的末尾
        # 定义条件: 当a指针和b指针都不超过字符串最末尾位置的时候
        while index_a < lens_1 and index_b < lens_2:
            # 先把word1中的字符加到result里面去
            result.append(word1[index_a])
            # 再把word2中的字符加到result里面去
            result.append(word2[index_b])

            # 更新word1中的指针位置，即向后移一位
            index_a += 1
            # 更新word2中的指针位置，即向后移一位
            index_b += 1
        

        '''
         这个时候, index_a 或 index_b中的一个已经到大了对应字符串的末尾
         问题是我们并不知道是index_a还是index_b。
        '''

        # 如果是index_a没有到达word1的末尾，即：指针小于word1的长度
        # Notice: 因为是在21行之后的26行更新位置，所以这里的判别条件是小于lens_1
        if index_a < lens_1:
            # 把word1中的剩余部分加到result里面
            result.append(word1[index_a:])
        
        # 如果是index_b没有到达word2的末尾
        if index_b < lens_2:
            # 把word2中的剩余部分加到result里面
            result.append(word2[index_b:])

        '''
         由于最后输出的要求是字符串, 这里调用join方法把
         所有的字符拼在一起输出
        '''        
        return ''.join(result)
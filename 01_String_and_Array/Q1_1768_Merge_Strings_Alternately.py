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
        # 定义两个指针，index_a 用于指向 word1 的当前字符位置，index_b 用于指向 word2 的当前字符位置
        index_a, index_b = 0, 0

        # 定义一个列表，用于存储交替合并后的字符
        result = []

        # 获取两个字符串的长度，分别存储在 lens_1 和 lens_2 中
        lens_1, lens_2 = len(word1), len(word2)

        # 当两个指针都没有超过各自字符串的长度时，继续进行交替合并
        while index_a < lens_1 and index_b < lens_2:
            # 从 word1 中取出当前指针指向的字符，并将其添加到结果列表中
            result.append(word1[index_a])
            # 从 word2 中取出当前指针指向的字符，并将其添加到结果列表中
            result.append(word2[index_b])

            # 更新指针，index_a 向后移动一位，以便指向下一个字符
            index_a += 1
            # 更新指针，index_b 向后移动一位，以便指向下一个字符
            index_b += 1
        
        '''
         到这里时，可能有一个指针已经到达其对应字符串的末尾。
         需要检查是哪个指针到达了末尾。
        '''

        # 如果 index_a 还没有到达 word1 的末尾，说明 word1 还有剩余字符
        if index_a < lens_1:
            # 将 word1 中剩余的部分（从 index_a 到结束）添加到结果列表中
            result.append(word1[index_a:])
        
        # 如果 index_b 还没有到达 word2 的末尾，说明 word2 还有剩余字符
        if index_b < lens_2:
            # 将 word2 中剩余的部分（从 index_b 到结束）添加到结果列表中
            result.append(word2[index_b:])

        '''
         最后，使用 ''.join(result) 将列表中的所有字符拼接成一个字符串并返回
        '''        
        return ''.join(result)
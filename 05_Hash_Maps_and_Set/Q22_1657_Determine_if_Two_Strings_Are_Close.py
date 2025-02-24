'''
1657. Determine if Two Strings Are Close

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

'''

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str  # 输入字符串1
        :type word2: str  # 输入字符串2
        :rtype: bool  # 返回布尔值，指示两个字符串是否可以通过重排列字符变为相同
        """
        # 如果两个字符串的长度不一样，直接返回 False
        if len(word1) != len(word2):
            return False

        # 初始化字符频率字典
        count1 = {}
        count2 = {}

        # 统计word1中每个字符的出现频率
        for char in word1:
            count1[char] = count1.get(char, 0) + 1
        
        # 统计word2中每个字符的出现频率
        for char in word2:
            count2[char] = count2.get(char, 0) + 1
        
        # 比较字符集和频率集
        return (set(count1.keys()) == set(count2.keys()) and  # 比较字符是否相同
                sorted(count1.values()) == sorted(count2.values()))  # 比较频率是否相同
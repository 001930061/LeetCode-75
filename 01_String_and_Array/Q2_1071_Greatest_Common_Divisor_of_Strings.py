'''
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if 
s = t + t + t + ... + t + t (i.e., t is concatenated with itself 
one or more times).

Given two strings str1 and str2, return the largest string x such 
that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
'''

'''
要解决这个问题, 我们首先需要了解欧几里得算法(辗转相除法)
即gcd(a, b) = gcd(b, a mod b)
直到b==0, 此时a就是最大公约数

这里使用欧几里得算法的目的就是寻找substring的长度, 用于最后获取结果。

接下来我们还要思考一个问题, 如果string1和string2是满足题目要求的那么无论拼接顺序怎么样,
把两个string拼在一起的时候应该是一样的, 如果不一样, 那么说明这两个string不符合条件。

下面我们开始写代码
'''

# ---------------- Final Answer: Time Complexity = O(n+m), Space Complexity = O(1)---------------- #
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        # 这里定义一个欧几里得算法
        def gcd(a, b):

            # b不等于0的时候
            while b:
                # 辗转相处法
                a, b = b, a % b
            
            # 最后返回最大公约数
            return a
        
        # 如果两个字符串拼接的顺序会影响拼接的结果
        # 那么这两个字符串不存在最大公约string
        if str1 + str2 != str2 + str1:
            return ''

        # 获取最大公约string的长度
        gcd_lens = gcd(len(str1), len(str2))

        # 这里直接从某一个string上截取这个长度并返回就可以了
        return str1[:gcd_lens]
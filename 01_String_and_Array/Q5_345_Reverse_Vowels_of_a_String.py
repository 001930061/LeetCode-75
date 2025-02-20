'''
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, 
more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"
'''

'''
这题的主要思路就是希望我们能把string中的元音字母的顺序颠倒一下:

刚一看到这一题的时候有两个想法:
1. 用dictionary, 找出所有元音所在的位置, 颠倒一下顺序, 再塞回去 - 颠倒位置困难
2. 有没有一个数据结构可以first in last out是不是就可以直接颠倒位置了? - Stack结构

OK, 那么现在我们只需要遍历两次string:
1. 如果是元音, 添加到stack里面
2. 如果是元音, 从stack里面拿出来赋值
'''

# ---------------- Final Answer: Time Complexity = O(n), Space Complexity = O(n)---------------- #

'''
错误答案
'''

'''
class Solution_Wrong(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 我们先定义元音字母
        vowels = 'aeiouAEIOU'

        # 我们再把string打散成list
        string = list(s)

        # 定义一个list
        stack = []

        # 下面我们第一次遍历这个string
        for char in string:
            # 如果遇到的是元音
            if char in vowels:
                # 把元音加到stack里面，从后面加
                stack.append(char)
        
'''
        # 这里错在char是局部变量, 它赋值的改变并不会影响string里面值的改变
'''
        # 下面我们第二次遍历这个string
        for char in string:
            # 如果遇到元音
            if char in vowels:
                # 把stack最上面的那一个拿出来赋值
                char = stack.pop(-1)
        
        # 拼接并返回字符串
        return ''.join(string)

'''


'''
正确答案
'''
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 首先我们定义元音字母
        vowels = 'aeiouAEIOU'

        # 然后我们打散这个string
        string = list(s)

        # 接着我们定义一个stack，实际是个list,然后进行第一次遍历
        stack = [char for char in string if char in vowels]

        # 我们这里进行第二次遍历，注意这里使用index而非char
        for i in range(len(string)):
            # 如果遇到了元音
            if string[i] in vowels:

                # stack最末尾的字符拿出来更改string上元音字母的赋值
                string[i] = stack.pop(-1)
        
        # 拼接并返回字符串
        return ''.join(string)

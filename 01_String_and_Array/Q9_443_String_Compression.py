'''
443. String Compression

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, 
be stored in the input character array chars. Note that group lengths that are 10 or 
longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
'''

'''
我们先遍历数组
我们需要找到每个重复字母的sublist, 把这个字母单独记成1, 然后数个数, 
如果个数大于一才开始计数, 我们需要记下的是位数而不是真正的个数
'''

# ---------------- Final Answer: Time Complexity = O(n), Space Complexity = O(1)---------------- #

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]  # 输入的字符列表
        :rtype: int             # 返回压缩后的字符长度
        """

        writer = 0  # 用于记录压缩后的字符写入位置
        reader = 0  # 用于遍历原字符列表的指针

        # 开始遍历字符列表
        while reader < len(chars):
            # 记录当前字符
            current_char = chars[reader]
            # 初始化计数器
            count = 0

            # 查找连续相同的字符
            while reader < len(chars) and current_char == chars[reader]:
                # 更新计数器
                count += 1
                # 移动读取指针到下一个字符
                reader += 1
            
            '''此时已经遇到了新的字符'''
            # 将当前字符写入到压缩后的字符列表中
            chars[writer] = current_char
            # 移动写入指针到下一个位置
            writer += 1

            # 如果计数大于1，表示有多个相同的字符，需要写入计数
            if count > 1:
                # 将计数拆分为字符串形式，逐个字符写入
                for digit in str(count):
                    # 将数字写入压缩后的字符列表
                    chars[writer] = digit
                    # 移动写入指针到下一个位置
                    writer += 1

        # 返回压缩后字符的长度
        return writer
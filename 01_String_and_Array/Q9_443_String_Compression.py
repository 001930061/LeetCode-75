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
        :type chars: List[str]
        :rtype: int
        """

        writer = 0 # 用来计数结果长度
        reader = 0 # 用来锁定index在chars的位置

        # 检索一遍chars
        while reader < len(chars):

            # 先收集目前的char
            current_char = chars[reader]
            # 初始化个数为0
            count = 0

            # 在chars的范围内，找连续的相同chars
            while reader < len(chars) and current_char == chars[reader]:
                # 计数更新
                count += 1
                # 读取位置更新
                reader += 1
            
            '''此时已经遇到了新的char'''
            # 更新新的char
            chars[writer] = current_char
            # 写的位置更新
            writer += 1

            # 如果计数大于1，意味着我们需要写到结果里
            if count > 1:
                # 把数字拆散成一个一个字符串
                for digit in str(count):

                    # 写进结果里面
                    chars[writer] = digit
                    # 更新写的位置
                    writer += 1

        # 返回结果
        return writer
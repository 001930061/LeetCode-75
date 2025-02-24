'''
605. Can Place Flowers
You have a long flowerbed in which some of the plots are planted, 
and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed without 
violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
'''

'''
这个问题的主要想要指导flowerbed上可以种花的位置个数量是不是小于等于n的。

如果我们不需要种花, 即n=0, 那么是不是直接返回True就可以了?

那么我们就需要遍历这个flowerbed寻找所有可以种花的位置的数量。
空位的要求是前后都不能种花, 特殊情况是首尾的位置上只要一边没有种花就可以了。

这里需要注意一下, 我们如果判定一个位置可以种花, 那么他的下一个位置就不可以种花了, 所以我们就需要跳过它。

统计所有可以种花的位置的数量然后和n对比, 返回对比结果。
'''




# ---------------- Final Answer: Time Complexity = O(n), Space Complexity = O(1)---------------- #



'''
错误答案
'''

'''
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        # 如果不许要种花, 直接返回True
        if n == 0:
            return True
        
        # 获取flowerbed的长度
        length = len(flowerbed)
        
        # 对可以种花的位置计数
        count = 0

        # 遍历flowerbend
        for i in range(length):
            if flowerbed[i] == 0 and i == 0 and flowerbed[i + 1] == 0:  # 这里的i+1可能会出现key error
                count += 1
                flowerbed[i] = 1
            
            if flowerbed[i] == 0 and i == length - 1 and flowerbed[i - 1] == 0: 这里的i-1可能会出现key error
                count += 1
                flowerbed[i] = 1
            
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0: 
                count += 1
                flowerbed[i] = 1


            # 以上最大的问题是它没有跳过可以种花位置的下一个位置，会导致重复计算。
        
        return count >= n

'''

'''
正确答案
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]  # 表示花坛，1表示已有花，0表示空地
        :type n: int                 # 需要种植的花的数量
        :rtype: bool                 # 返回是否可以种下 n 朵花
        """

        # 如果不需要种花，直接返回 True
        if n == 0:
            return True
        
        # 获取花坛的长度，用于后续的索引检索
        length = len(flowerbed)

        # 用于记录可以种花的位置数量
        count = 0

        # 遍历花坛上所有的位置
        for i in range(length):

            # 如果当前位置是空着的（0）
            if flowerbed[i] == 0:

                # 检查左边的位置是否为空
                left_empty = (i == 0 or flowerbed[i-1] == 0)
                # 检查右边的位置是否为空
                right_empty = (i == length - 1 or flowerbed[i+1] == 0)

                # 如果左右都是空着的，可以种花
                if left_empty and right_empty:
                    # 在当前位置种下花（标记为1）
                    flowerbed[i] = 1
                    # 更新可种花的数量
                    count += 1

                    # 跳过下一个位置，避免相邻种花
                    i += 1
            
        # 最后，比较可以种花的位置数量和需要的数量
        return count >= n


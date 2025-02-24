'''
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such 
that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container 
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''

'''
这一题我们是可以pop这个height来对这个height进行破坏的

我们需要两个指针来分别从开头和末尾来做面积的计算
'''

# ----------------------------------------------------------------------------------

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]  # 输入的高度列表，表示每根柱子的高度
        :rtype: int  # 返回值为最大面积
        """

        # 定义一个左指针，初始化位置为列表的开头
        left = 0
        # 定义一个右指针，初始化位置为列表的末尾
        right = len(height) - 1

        # 初始化最大面积为0
        max_area = 0

        # 如果height的列表长度小于1，那么没法计算面积，直接返回0
        if len(height) <= 1:
            return 0

        # 当两个指针没有相交的时候
        while left < right:
            # 计算目前的面积
            current_area = min(height[left], height[right]) * (right - left)

            # 如果当前面积更大，那就更新最大面积
            if current_area > max_area:
                max_area = current_area
            
            # 找左右两个指针哪个是短板，把短板往中间移动
            if height[left] <= height[right]:
                left += 1  # 移动左指针
            else:
                right -= 1  # 移动右指针

        # 返回最大面积
        return max_area
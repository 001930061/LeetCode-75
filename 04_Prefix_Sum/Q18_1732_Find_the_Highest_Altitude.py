'''
1732. Find the Highest Altitude

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

 

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
 

Constraints:

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100
'''

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]  # 输入的高度变化数组
        :rtype: int  # 返回最高的海拔高度
        """
        sum = 0  # 初始化当前高度为0
        max_h = 0  # 初始化最大高度为0

        # 遍历高度变化数组
        for i in range(len(gain)):
            sum += gain[i]  # 更新当前高度
            max_h = max(max_h, sum)  # 更新最大高度，比较当前高度和最大高度

        return max_h  # 返回最大高度
'''
1431. Kids With the Greatest Number of Candies

There are n kids with candies. You are given an integer array candies, 
where each candies[i] represents the number of candies the ith kid has, 
and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, 
after giving the ith kid all the extraCandies, they will have the greatest 
number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
Example 3:

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
'''


'''
要解决这个问题, 我们首先要知道Kids中目前拥有最多candy的那一个, 手里有多少candy.

然后我们遍历所有kids, 把他们手中的candy+bonus candy 看是不是大于等于这个max.
'''

# ---------------- Final Answer: Time Complexity = O(n), Space Complexity = O(n)---------------- #

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]  # 孩子们手中原有的糖果数量
        :type extraCandies: int    # 额外的糖果数量
        :rtype: List[bool]         # 返回一个布尔值列表，表示每个孩子是否能拥有最多的糖果
        """

        # 首先，我们需要找到孩子中手上最多糖果的数量
        max_candy = max(candies)  # 使用 max 函数找到最大糖果数量

        # 接着，我们使用列表推导式创建一个布尔值列表
        # 遍历每个孩子手上的糖果数量，如果该孩子手上的糖果加上额外的糖果大于等于最大糖果数量，则为 True；否则为 False
        return [candy + extraCandies >= max_candy for candy in candies]
'''
2215. Find the Difference of Two Arrays

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000
'''
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]  # 第一个整数列表
        :type nums2: List[int]  # 第二个整数列表
        :rtype: List[List[int]]  # 返回两个列表，分别包含两个列表的差异
        """

        # 将输入列表转换为集合，以便于进行集合运算
        nums1 = set(nums1)
        nums2 = set(nums2)

        # 计算 nums1 中有但 nums2 中没有的元素
        result1 = nums1 - nums2
        # 计算 nums2 中有但 nums1 中没有的元素
        result2 = nums2 - nums1

        # 将结果转换为列表并返回
        return [list(result1), list(result2)]

# -*- coding:utf-8 -*-

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int])->float:
        m,n = len(nums1),len(nums2)
        len_new = m + n
        nums1.extend(nums2)
        new_nums = nums1
        if len_new == 1:
            return float(new_nums[0])
        new_nums = sorted(new_nums)
        con = len_new % 2
        if con == 0:
            index1 = len_new // 2
            index2 = (len_new // 2) + 1
            median = (new_nums[index1-1] + new_nums[index2-1]) / 2
        else:
            index = (len_new + 1) // 2
            median = new_nums[index-1] 
        return float(median)
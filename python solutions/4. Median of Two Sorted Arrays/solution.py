"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        sorted_nums = list()
        while (i != len(nums1) or j != len(nums2)):
            if i == len(nums1):
                while j != len(nums2):
                    sorted_nums.append(nums2[j])
                    j+=1
            elif j == len(nums2):
                while i != len(nums1):
                    sorted_nums.append(nums1[i])
                    i+=1
            elif nums1[i] < nums2[j]:
                sorted_nums.append(nums1[i])
                i+=1
            else:
                sorted_nums.append(nums2[j])
                j+=1
        if not len(sorted_nums)%2:
            print(len(sorted_nums)//2)
            return ((sorted_nums[len(sorted_nums)//2] + sorted_nums[(len(sorted_nums)//2)-1])/2)
        else:
            return sorted_nums[len(sorted_nums)//2]


#https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_pointer = m - 1
        nums2_pointer = n - 1

        merged_pointer = m + n - 1
        while merged_pointer >= 0:
            if nums1_pointer >= 0 and (nums2_pointer < 0 or nums1[nums1_pointer] > nums2[nums2_pointer]):
                nums1[merged_pointer] = nums1[nums1_pointer]
                nums1_pointer -= 1
            else:
                nums1[merged_pointer] = nums2[nums2_pointer]
                nums2_pointer -= 1
            merged_pointer -= 1

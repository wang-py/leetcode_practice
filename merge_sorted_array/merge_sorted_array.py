class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        len1 = len(nums1)
        len2 = len(nums2)
        for i in range(len2):
            if nums1[-i] < nums2[-i]:
                temp = nums2[-i]
                nums1[-i] = nums2[-i]

        print("result:", nums1)


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    sol = Solution()
    sol.merge(nums1, m, nums2, n)

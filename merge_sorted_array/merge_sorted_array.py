class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = m - 1
        if a < 0:
            a = 0
            b = 0
            c = 0
            if nums1[a] < nums2[b]:
                nums1[c] = nums2[b]
            else:
                nums1[c] = nums1[a]
                nums1[a] = nums2[b]
        for c in range(m + n - 1, 0, -1):
            b = c - m
            if b < 0:
                b = 0
            if nums1[a] < nums2[b]:
                nums1[c] = nums2[b]
            else:
                nums1[c] = nums1[a]
                nums1[a] = nums2[b]
                a -= 1

        print("result:", nums1)


if __name__ == "__main__":
    nums1 = [0]
    nums2 = [1]
    m = 0
    n = 1
    sol = Solution()
    sol.merge(nums1, m, nums2, n)

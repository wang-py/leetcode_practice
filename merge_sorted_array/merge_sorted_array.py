class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = m - 1
        b = n - 1
        c = m + n - 1

        while b >= 0:
            if nums1[a] > nums2[b] and a >= 0:
                nums1[c] = nums1[a]
                a -= 1
            else:
                nums1[c] = nums2[b]
                b -= 1
            c -= 1

        print("result:", nums1)


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [4, 5, 6]
    m = 3
    n = 3
    sol = Solution()
    sol.merge(nums1, m, nums2, n)

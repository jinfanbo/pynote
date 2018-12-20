class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = [x for x in A if x % 2 == 0]
        odd = [x for x in A if x % 2 != 0]
        return even + odd


if __name__ == '__main__':
    a = Solution()
    print(a.sortArrayByParity([3, 1, 2, 4]))

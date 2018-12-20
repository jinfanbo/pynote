class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for index, lst in enumerate(A):
            # print(index, lst, sep='\n')
            A[index] = [1 if x == 0 else 0 for x in lst[::-1]]
        return A


if __name__ == '__main__':
    a = Solution()
    print(a.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
    # a.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])

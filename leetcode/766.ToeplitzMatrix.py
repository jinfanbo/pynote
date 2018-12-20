class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row = len(matrix)
        i = 0
        while i + 1 < row:
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
            i += 1
        return True


if __name__ == '__main__':
    a = Solution()
    print(a.isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
    print(a.isToeplitzMatrix([[1, 2], [2, 2]]))

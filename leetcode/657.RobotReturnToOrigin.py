class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        U_count = moves.count('U')
        D_count = moves.count('D')
        L_count = moves.count('L')
        R_count = moves.count('R')
        if U_count == D_count and L_count == R_count:
            return True
        else:
            return False


if __name__ == '__main__':
    a = Solution()
    a.judgeCircle('DD')

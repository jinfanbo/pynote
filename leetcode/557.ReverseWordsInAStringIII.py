class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_s = ' '.join(x[::-1] for x in s.split())
        return new_s


if __name__ == '__main__':
    a = Solution()
    print(a.reverseWords("Let's take LeetCode contest"))

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                   "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
        hash_letter = dict(zip(letter, letters))
        codes = set()
        for l in words:
            code = ''
            for i in l:
                code = code + hash_letter[i]
            codes.add(code)
        return len(codes)


if __name__ == '__main__':
    a = Solution()
    a.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])

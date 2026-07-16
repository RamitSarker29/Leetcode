class Solution:
    def reverseWords(self, s: str) -> str:

        result = []

        left = 0
        right = 0

        while right <= len(s):

            if right == len(s) or s[right] == " ":

                word = s[left:right]

                result.append(word[::-1])

                left = right + 1

            right += 1

        return " ".join(result)
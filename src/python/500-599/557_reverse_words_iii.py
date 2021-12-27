"""
Solution to 557. Reverse Words in a String III (https://leetcode.com/problems/reverse-words-in-a-string-iii/)
Difficulty:     EASY
Runtime:        O(n) - Linear time
Space:          O(n) - Linear space
Submission:     https://leetcode.com/submissions/detail/607753258/
"""
__author__      = "jagwirecode"

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverses each word in a string whilst maintaining the relative order of the words
        Eg. "Hello World!" becomes "olleH !dlroW"

        Args:
            s (str): String to be reversed

        Returns:
            str: Reversed string
        """
        # Tokenise words in the string by space
        wordArray = s.split(" ")
        
        # Enumerate through the tokens, reversing each one
        for i, word in enumerate(wordArray):
            # Python voodoo magic, where the current index has it's token reversed
            # ::-1 means slice whole element, but go by -1 aka backwards, effectively reversing the element
            wordArray[i] = word[::-1]

        # Reassemble the string by joining each reversed token separated by spaces                                    
        return " ".join(wordArray)
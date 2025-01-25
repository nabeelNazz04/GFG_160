'''
Non Repeating Character:

Given a string s consisting of lowercase Latin Letters. Return the first non-repeating character in s. If there is no non-repeating character, return '$'.
Note: When you return '$' driver code will output -1.

Examples:

Input: s = "geeksforgeeks"
Output: 'f'
Explanation: In the given string, 'f' is the first character in the string which does not repeat.
'''
class Solution:
    
    # Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self, s):
        # Dictionary to store the frequency of each character.
        non = {}
        for ch in s:
            non[ch] = non.get(ch, 0) + 1
        
        # Iterating through the string to find the first non-repeating character.
        for ch in s:
            if non[ch] == 1:
                return ch
        return "$"  # Return "$" if no non-repeating character is found.
if __name__=="__main__":
    c=Solution()
    s=s = "geeksforgeeks"
    print(c.nonRepeatingChar(s))
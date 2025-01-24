### Anagram:

class Solution:
    
    # Function to check whether two strings are anagrams of each other or not
    def areAnagrams(self, s1, s2):
        # Use hashmap to count character frequencies
        charCount = {}
        for ch in s1:
            charCount[ch] = charCount.get(ch, 0) + 1
        for ch in s2:
            charCount[ch] = charCount.get(ch, 0) - 1
        for value in charCount.values():
            if value != 0:
                return False
        return True

if __name__ == "__main__":
    s1 = "geeks"
    s2 = "skeeg"
    
    # Create an instance of the Solution class
    s = Solution()
    print(s.areAnagrams(s1, s2))  # Output: True

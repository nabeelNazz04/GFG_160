# KMP algorithm for pattern string
# if you add the string to itself all the possible rotations will appear on that
def constructLps(pat, lps):
    len_ = 0  # Length of the longest prefix suffix
    m = len(pat)  # Length of the pattern
    lps[0] = 0  # LPS value for the first character is always 0
    i = 1  # Start from the second character

    while i < m:
        if pat[i] == pat[len_]:
            len_ += 1
            lps[i] = len_
            i += 1
        else:
            if len_ != 0:
                len_ = lps[len_ - 1]  # Adjust len_ using the LPS array
            else:
                lps[i] = 0
                i += 1

class Solution:
    def search(self, pat, txt):
        n = len(txt)  # Length of the text
        m = len(pat)  # Length of the pattern
        lps = [0] * m  # Initialize LPS array
        res = []  # List to store the starting indices of matches

        constructLps(pat, lps)  # Construct the LPS array

        i = 0  # Index for text
        j = 0  # Index for pattern

        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1
                if j == m:
                    res.append(i - j)  # Match found, record the starting index
                    j = lps[j - 1]  # Adjust j using the LPS array
            else:
                if j != 0:
                    j = lps[j - 1]  # Adjust j using the LPS array
                else:
                    i += 1  # No match, move to the next character in the text

        return res  # Return the list of starting indices
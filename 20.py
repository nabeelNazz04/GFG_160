# Function to compute the Longest Prefix Suffix (LPS) array for the KMP algorithm
def computeLPSArray(pat):
    """
    This function computes the LPS (Longest Prefix Suffix) array for the pattern string `pat`.
    The LPS array helps in determining how much we can skip while matching the pattern in the text.

    Parameters:
    - pat: The pattern string.

    Returns:
    - lps: A list containing the LPS values.
    """
    n = len(pat)
    lps = [0] * n  # Initialize the LPS array with zeroes.
    patLen = 0  # Length of the previous longest prefix suffix.
    i = 1  # Start iterating from the second character of the pattern.

    while i < n:
        # If characters match, extend the current LPS length.
        if pat[i] == pat[patLen]:
            patLen += 1
            lps[i] = patLen
            i += 1
        else:
            # If characters don't match, backtrack the LPS length.
            if patLen != 0:
                patLen = lps[patLen - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

class Solution:
    """
    This class contains a method to check if two strings are rotations of each other.
    """

    # Function to check if two strings are rotations of each other or not.
    def areRotations(self, s1, s2):
        """
        This function checks if string `s2` is a rotation of string `s1`.
        It uses the KMP string matching algorithm.

        Parameters:
        - s1: The first string.
        - s2: The second string.

        Returns:
        - True if `s2` is a rotation of `s1`, otherwise False.
        """
        # Concatenate s1 with itself to account for rotations.
        txt = s1 + s1
        pat = s2

        # If lengths differ, s2 cannot be a rotation of s1.
        if len(s1) != len(s2):
            return False

        n = len(txt)  # Length of the concatenated string.
        m = len(pat)  # Length of the pattern string.
        lps = computeLPSArray(pat)  # Compute the LPS array for the pattern.

        i = 0  # Pointer for the text string.
        j = 0  # Pointer for the pattern string.

        # Start the KMP string matching algorithm.
        while i < n:
            # If characters match, move both pointers forward.
            if pat[j] == txt[i]:
                j += 1
                i += 1
            
            # If we have matched the entire pattern, s2 is a rotation of s1.
            if j == m:
                return True

            # If characters don't match after a partial match, adjust `j` using LPS.
            elif i < n and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        # If we reach here, s2 is not a rotation of s1.
        return False


def main():
    """
    Main function to test the `areRotations` function.
    """
    # Input strings
    s1 = "ABCD"
    s2 = "CDAB"

    # Create an instance of the Solution class.
    solution = Solution()

    # Check if s2 is a rotation of s1.
    if solution.areRotations(s1, s2):
        print(f"'{s2}' is a rotation of '{s1}'.")
    else:
        print(f"'{s2}' is NOT a rotation of '{s1}'.")

# Run the main function.
if __name__ == "__main__":
    main()

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0  # Initialize left pointer to the first index
        right = len(s) - 1  # Initialize right pointer to the last index

        while left < right:
            # Move left pointer past non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1

            # Move right pointer past non-alphanumeric characters
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False  # Mismatch found, not a palindrome

            # Move pointers inward
            left += 1
            right -= 1

        return True  # All characters matched, it's a palindrome

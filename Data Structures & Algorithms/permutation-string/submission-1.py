class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        
        # If s1 is longer than s2, s2 cannot contain a permutation of s1
        if n1 > n2:
            return False
        
        # Frequency count for target string s1
        s1_count = Counter(s1)
        # Initial frequency count for the first window of size n1 in s2
        window_count = Counter(s2[:n1])
        
        # Check if the very first window is a match
        if s1_count == window_count:
            return True
        
        # Slide the window across s2 one character at a time
        for i in range(n1, n2):
            # Add the new character entering the window on the right
            window_count[s2[i]] += 1
            
            # Remove/decrement the character leaving the window on the left
            left_char = s2[i - n1]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
            
            # Compare current window frequencies with target frequencies
            if window_count == s1_count:
                return True
                
        return False
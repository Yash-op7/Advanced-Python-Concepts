class Solution:
    def getLucky(self, s: str, k: int) -> int:
        """
        Convert the string s into an integer by replacing each letter with its position in the alphabet.
        Perform the digit sum transformation k times and return the final result.

        :param s: Input string consisting of lowercase English letters.
        :param k: Number of times to apply the digit sum transformation.
        :return: Resulting integer after k transformations.
        """
        # Convert the string to a numeric string based on alphabet positions.
        numeric_string = ''.join(str(ord(c) - ord('a') + 1) for c in s)

        # Perform the transformation k times
        for _ in range(k):
            # Sum the digits of the current numeric string
            numeric_sum = sum(int(digit) for digit in numeric_string)
            numeric_string = str(numeric_sum)
        
        return int(numeric_string)

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        converted_string = ''.join([str(ord(c) - ord('a') + 1) for c in s])

        while k > 0:
            sum = 0
            for c in converted_string:
                sum += int(c)
            k -= 1
            converted_string = str(sum)
            
        return int(converted_string)
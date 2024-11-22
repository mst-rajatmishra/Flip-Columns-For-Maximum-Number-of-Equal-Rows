from collections import defaultdict
from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # Initialize a dictionary to store the count of identical row patterns
        pattern_count = defaultdict(int)
        
        # Iterate through each row in the matrix
        for row in matrix:
            # Create a pattern for the current row, considering the flipped version
            # Generate a "flip-mask" for the row
            pattern = tuple(row)  # The original row itself
            flipped_pattern = tuple(1 - x for x in row)  # Flipped version of the row
            
            # Update the count for both the original and flipped pattern
            pattern_count[pattern] += 1
            pattern_count[flipped_pattern] += 1
        
        # Return the maximum number of rows that can be made equal by flipping columns
        return max(pattern_count.values())

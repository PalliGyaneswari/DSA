class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        # Initialize variables
        left = 0  # Left pointer of the sliding window
        max_freq = 1  # At least one element has a frequency of 1
        current_operations = 0  # The number of operations used
        
        # Iterate over the array with the right pointer
        for right in range(len(nums)):
            # Increment the total cost to make nums[right] equal to nums[right] (it's a self cost)
            current_operations += (nums[right] - nums[right - 1]) * (right - left)
            
            # If we exceed the allowed operations, shrink the window from the left
            while current_operations > k:
                current_operations -= (nums[right] - nums[left])
                left += 1
            
            # Update the maximum frequency
            max_freq = max(max_freq, right - left + 1)
        
        return max_freq
            
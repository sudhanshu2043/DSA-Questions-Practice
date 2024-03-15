class Solution:
    # Function to find the number of ways to partition an array into two subsets
    # with a given target difference using dynamic programming
    def findWays(self,num, tar):
        n = len(num)

        # Initialize a list 'prev' to store results for the previous element
        prev = [0 for i in range(tar + 1)]

        # Initialize 'prev' based on the first element of 'num'
        if num[0] == 0:
            prev[0] = 2  # Two cases - pick and not pick
        else:
            prev[0] = 1  # One case - not pick

        if num[0] != 0 and num[0] <= tar:
            prev[num[0]] = 1  # One case - pick

        for ind in range(1, n):
            # Initialize a list 'cur' to store results for the current element
            cur = [0 for i in range(tar + 1)]
            for target in range(tar + 1):
                notTaken = prev[target]

                taken = 0
                if num[ind] <= target:
                    taken = prev[target - num[ind]]

                # Store the result in 'cur' with modulo operation
                cur[target] = (notTaken + taken) 
            prev = cur

        # Return the result for the target sum
        return prev[tar]
    def findTargetSumWays(self, arr: List[int], target: int) -> int:
        totSum = 0
        n=len(arr)
        for i in range(n):
            totSum += arr[i]

        # Checking for edge cases
        if (totSum - target) < 0 or ((totSum - target) % 2):
            return 0

        # Calculate and return the number of ways using 'findWays' function
        return self.findWays(arr, (totSum - target) // 2)
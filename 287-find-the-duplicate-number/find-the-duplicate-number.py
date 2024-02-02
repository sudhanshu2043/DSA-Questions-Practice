class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # TC: O(N)+O(NlogN)
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i-1]==nums[i]:
        #         return nums[i]
        
        #Method 2: TC:O(N)
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Detect the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find the duplicate number
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
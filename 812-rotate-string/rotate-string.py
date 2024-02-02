class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        a=s+s
        # this will take additional O(N) because .find() take O(N) in worst case
        # if a.find(goal)!=-1:
        #     return True
        # else:
        #     return False
        return goal in a
        # in take linear complexity
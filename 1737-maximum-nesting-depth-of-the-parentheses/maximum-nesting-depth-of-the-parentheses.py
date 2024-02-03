class Solution(object):
    def maxDepth(self, s):
        res,curr=0,0
        for i in range(len(s)):
            if(s[i]=='('):
                curr+=1
                res=max(res,curr)
            if(s[i]==')'):
                curr-=1
        return res
        
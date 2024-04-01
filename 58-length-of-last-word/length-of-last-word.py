class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # x=s.split()
        # return len(x[-1])
        flag=ans=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ' and flag:
                break
            if s[i]!=' ':
                ans+=1
                flag=1
        return ans
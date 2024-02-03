class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        lastCh=s[len(s)-1]
        res=my_dict.get(lastCh)
        for i in range(len(s)-2,-1,-1):
            ch=s[i]
            nt=s[i+1]
            if my_dict.get(ch)<my_dict.get(nt):
                res=res-my_dict.get(ch)
            else:
                res+=my_dict.get(ch)
        return res
from collections import defaultdict

class Solution:
    def beauty(self, alpha: list) -> int:
        lf = float('-inf')
        mf = -1
        for i in range(len(alpha)):
            mf = max(mf, alpha[i])
            if alpha[i] >= 1:
                lf = min(lf, alpha[i])
        return mf - lf

    def beautySum(self, s: str) -> int:
        # res = 0
        # for i in range(len(s)):
        #     alpha = [0] * 26
        #     for j in range(i, len(s)):
        #         alpha[ord(s[j]) - ord('a')] += 1
        #         res = res + self.beauty(alpha)
        # return res
        ans = 0 
        for i in range(len(s)):
            freq = [0]*26
            for j in range(i, len(s)):
                freq[ord(s[j])-97] += 1
                ans += max(freq) - min(x for x in freq if x)
        return ans 
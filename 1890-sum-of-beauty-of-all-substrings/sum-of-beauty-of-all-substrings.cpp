class Solution {
public:
    // int beautySum(string s) {
    //     int ans=0;
    //     int n=s.length();
    //     for(int i=0;i<n;i++){
    //         unordered_map<char,int> mpp;
    //         multiset<int> st;
    //         for(int j=i;j<n;j++){
    //             if(mpp.find(s[j])!=mpp.end()){
    //                 st.erase(st.find(mpp[s[j]]));
    //             }
    //             mpp[s[j]]++;
    //             st.insert(mpp[s[j]]);
    //             ans+=(*st.rbegin()-*st.begin());
    //         }
    //     }
    //     return ans;
    // }
    int beauty(vector<int>& alpha) {
        int lf = 1e9;
        int mf = -1;
        for (int i = 0; i < alpha.size(); ++i) {
            mf = max(mf, alpha[i]);
            if (alpha[i] >= 1) {
                lf = min(lf, alpha[i]);
            }
        }
        return mf - lf;
    }

    int beautySum(string s) {
        int res = 0;
        for (int i = 0; i < s.length(); ++i) {
            vector<int> alpha(26, 0);
            for (int j = i; j < s.length(); ++j) {
                alpha[s[j] - 'a'] += 1;
                res += beauty(alpha);
            }
        }
        return res;
    }
};
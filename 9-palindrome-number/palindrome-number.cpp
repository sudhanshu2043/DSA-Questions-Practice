class Solution {
public:
    bool isPalindrome(int x) {
        int num=x;
        long revNum=0;
        while(x>0){
            int digit=x%10;
            revNum=(revNum*10)+digit;
            x=x/10;
        }
        if(num==revNum){
            return true;
        }
        else{
            return false;
        }
    }
};
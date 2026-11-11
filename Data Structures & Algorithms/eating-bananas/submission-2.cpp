class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1;
        int right = *max_element(piles.begin(),piles.end());
        int ans;
        while (left <= right){
            long long cnt = 0;
            int mid = (left + right)/2;
            for (int pile : piles){
                cnt += pile/mid;
                if (pile % mid != 0){
                    cnt++;
                }
            }
            if (cnt <= h){
                ans = mid;
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        return ans; 
    }
};

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int left = 0;
        int maxprofit = 0;
        for (int right = 1; right < prices.size();right++){
            while (prices[left] > prices[right] && left < right){
                left++;
            }
            maxprofit = max(maxprofit , prices[right] - prices[left]);
        }
        return maxprofit;
    }
};

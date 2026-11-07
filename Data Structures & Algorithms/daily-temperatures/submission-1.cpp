class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> st;
        vector<int> result(temperatures.size(),0);
        for (int i = 0 ; i<temperatures.size();i++) {
            while ((!st.empty())&&temperatures[i] > temperatures[st.top()]) {
                int previous = st.top();
                result[previous]=i-previous;
                st.pop();
            }
            st.push(i);
        }
    return result;
    }
};

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        int row = -1;
        int m_left = 0;
        int m_right = m-1;
        while (m_left <= m_right) {
            int mid = (m_left + m_right) / 2;
            if(target < matrix[mid][0]){
                m_right = mid -1;
            }
            else if (target > matrix[mid][n-1]){
                m_left = mid + 1;
            }
            else {
                row = mid;
                break;
            }
        }
        if (row == -1) return false;
        int n_left = 0;
        int n_right = n-1;
        while (n_left <= n_right) {
            int mid = (n_left + n_right) / 2;
            if (matrix[row][mid]==target) {
                return true;
            }
            else if(matrix[row][mid]>target){
                n_right = mid - 1;
            }
            else {
                n_left = mid + 1;
            }
        }
        return false;
    }
};

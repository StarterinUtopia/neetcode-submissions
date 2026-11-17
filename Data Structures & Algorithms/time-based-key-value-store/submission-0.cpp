class TimeMap {
    private:
    unordered_map<string,vector<pair<int,string>>> records;
public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        records[key].push_back({timestamp,value});
    }
    
    string get(string key, int timestamp) {
        auto& history =  records[key];
        int left = 0;
        int right = (int)history.size() - 1;
        string result = "";
        while (left <= right){
            int mid = (left + right) / 2;
            if (history[mid].first <= timestamp){
                result = history[mid].second;
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }   
        }
        return result;
    }
};

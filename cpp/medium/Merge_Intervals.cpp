class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> answer;
        vector<int> interval;
        sort(intervals.begin(), intervals.end());
        answer.push_back(intervals[0]);
        for (int i = 1; i < intervals.size(); ++i){
            interval = intervals[i];
            while(answer.size() != 0 && interval[0] <= answer.back()[1]) {
                cout << answer.size() << endl;
                interval[0] = min(answer.back()[0], interval[0]);
                interval[1] = max(answer.back()[1], interval[1]);
                answer.pop_back();
            }
            answer.push_back(interval);
        }
        return answer;
    }
};

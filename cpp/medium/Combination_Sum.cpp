class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> answer;
        vector<int> combination;
        layer(0, answer, candidates, target, combination);
        return answer;
    }
    void layer(int j, vector<vector<int>>& answer, vector<int>& candidates, int target, vector<int>& combination) {
        for (int i = j; i < candidates.size(); ++i){
            combination.push_back(candidates[i]);
            target-=candidates[i];
            // for (int n = 0; n < combination.size(); ++n){
            //     cout << combination[n] << ",";
            // }
            // cout << "; ";
            // cout << i << endl;
            if (target==0) {
                answer.push_back(combination);
                combination.pop_back();
                target+=candidates[i];
            }
            else if (target>0) {
                // vector<int> sub_candidates(candidates.begin()+i, candidates.end());
                layer(i, answer, candidates, target, combination);
                combination.pop_back();
                target+=candidates[i];
            }
            else{
                combination.pop_back();
                target+=candidates[i];
            }
        }
    }
};

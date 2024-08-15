class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int levels = triangle.size();
        for (int level = 1; level < levels; ++level) {
            for (int idx = 0; idx < triangle[level].size(); ++idx) {
                if (idx == 0) triangle[level][idx]+=triangle[level-1][0];
                else if (idx == triangle[level].size()-1) triangle[level][idx]+=triangle[level-1][idx-1];
                else triangle[level][idx]+=min(triangle[level-1][idx-1], triangle[level-1][idx]);
            }
        }
        return *min_element(triangle[levels-1].begin(), triangle[levels-1].end());
    }

};

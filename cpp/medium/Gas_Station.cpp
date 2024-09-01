class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        vector<int> gap;
        for (int i = 0; i < gas.size(); ++i) {
            gap.push_back(gas[i] - cost[i]);
        }
        if (accumulate(gap.begin(), gap.end(), 0) < 0) return -1;
        int start = 0;
        int gas_amount = 0;
        for (int i = 0; i < gap.size(); ++i) {
            gas_amount = gas_amount + gap[i];
            if (gas_amount < 0) {
                start = i + 1;
                gas_amount = 0;
            }
        }
        return start;
    }
};

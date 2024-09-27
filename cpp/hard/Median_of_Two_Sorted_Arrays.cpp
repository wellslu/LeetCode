class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        int cnt = m + n;
        int med =  (cnt % 2 == 0) ? cnt/2-1:cnt/2;
        int i = 0;
        int j = 0;
        double ans;
        for (int num = 0; num <= med; num++) {
            if (j == n || i < m && nums1[i] <= nums2[j]) {
                ans = nums1[i];
                i++;
            }
            else {
                ans = nums2[j];
                j++;
            }
            cout << ans;
        }
        
        if (cnt % 2 == 0) {
            if (j == n || i < m && nums1[i] <= nums2[j]) ans+=nums1[i];
            else ans+=nums2[j];
            ans/=2;
        }
        return ans;
    }
};

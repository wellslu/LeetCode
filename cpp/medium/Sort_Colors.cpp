class Solution {
public:
    void sortColors(vector<int>& nums) {
        quickSort(nums.begin(), nums.size());
    }
    void quickSort(vector<int>::iterator array, int n) {
        int pivot = array[n-1];
        int i = 0;
        int temp;
        for (int idx = 0; idx < n - 1; ++idx) {
            if (array[idx] < pivot) {
                temp = array[idx];
                array[idx] = array[i];
                array[i] = temp;
                i++;
            }
        }
        array[n-1] = array[i];
        array[i] = pivot;
        if (i > 0) {
            quickSort(array, i);
        }
        if (i < n-1) {
            quickSort(array + i + 1, n - i - 1);
        } 
    }
};

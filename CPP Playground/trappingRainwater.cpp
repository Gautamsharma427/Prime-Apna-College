#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int trap(vector<int> &height)
{
    int waterTrapped = 0;
    int leftMax = INT_MIN;
    int rightMax = INT_MIN;
    for (int i = 1; i < height.size() - 1; i++)
    {
        leftMax = max(leftMax, height[i]);

        int currentBar = height[i];
        waterTrapped = waterTrapped + max(0, min(leftMax, rightMax) - currentBar);
    }
    return waterTrapped;
}

int main() {
    vector<int> height = {7,54,0,2,34,32};
    trap(height);
};

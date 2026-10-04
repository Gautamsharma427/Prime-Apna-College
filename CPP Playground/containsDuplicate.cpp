#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    // Contains Duplicate 
    // 1. Scan the array for all elements
    // 2. check if element already exists in the array
    // 3. increase count if the element is spotted multiple times
    vector<int> arr = {1,2,3,4,5};
    int count=0;
    bool duplicate = false;
    for (int i = 0; i < arr.size(); i++)
    {
       int element = arr[i];
       int count = 0;
       for (int i = 0; i < arr.size(); i++)
       {
            if(element==arr[i]){
                count+=1;
            }
       }
       if(count>1){
        duplicate = true;
        break;
       }
    }
    cout<<duplicate;
}
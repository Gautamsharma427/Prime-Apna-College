// This file contains some code about arrrays
#include <iostream>
using namespace std;

int linearSearch(int *arr, int n, int num);
void reverseArray(int *arr, int size);
int main()
{
    int arr[] = {1, 2, 3, 4, 5, 7, 32, 343, 909, 9302};
    int size = sizeof(arr) / sizeof(arr[0]);
    cout << "value found at index " << linearSearch(arr, size, 32) << endl;
    reverseArray(arr,size);
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << endl;
    };
}
int linearSearch(int *arr, int n, int num)
{
    int ans = -1;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == num)
        {
            ans = i;
            return ans;
        }
    }
    return ans;
}
void reverseArray(int *arr, int size)
{
    int reversedArray[size];
    int count = 1;
    for (int i = 0; i < size; i++)
    {
        reversedArray[i] = arr[size - count];
        count++;
    }
    for (int i = 0; i < size; i++)
    {
        arr[i]=reversedArray[i];
    }
    
}   
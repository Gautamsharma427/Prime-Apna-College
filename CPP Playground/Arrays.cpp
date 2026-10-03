// This file contains some code about arrrays
#include <iostream>
using namespace std;

int linearSearch(int *arr, int n, int num);
int binarySearch(int *arr, int n, int num);
void reverseArray(int *arr, int size);
void binaryReverseArray(int *arr, int size);
void printSubArrays(int *arr, int size);
int main()
{
    // int arr[] = {1, 2, 3, 4, 5, 7, 32, 343, 909, 9302,89};
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]);
    cout << "value found at index " << linearSearch(arr, size, 3) << endl;
    cout << "value found at the index : " << binarySearch(arr, size, 3)<< endl;
    binaryReverseArray(arr, size);
    reverseArray(arr,size);
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << endl;
    };
    printSubArrays(arr,size);
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
int binarySearch(int *arr, int n, int num)
{
    int left = 0;
    int right = n - 1;
    while (left <= right)
    {

        int mid = (left+right) / 2;
        if (arr[mid] == num)
        {
            return mid;
        }
        else if (arr[mid] < num)
        {
            left = mid + 1;
        }
        else if (arr[mid] > num)
        {
            right = mid - 1;
        }
    }
    return -1;
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
        arr[i] = reversedArray[i];
    }
}
void binaryReverseArray(int *arr, int size)
{
    int n = size - 1;
    for (int i = 0; i < size; i++)
    {
        if (i >= n)
        {
            break;
        }
        else
        {
            int temp = arr[i];
            arr[i] = arr[n];
            arr[n] = temp;
            n--;
        }
    }
}
void printSubArrays(int *arr,int n){
   int numberOfSubarrays = n*(n+1)/2;
   for (int start = 0; start < n; start++)
   {
    for (int end = start; end < n; end++)
    {
        // cout<<"("<<start<<","<<end<<")"<<"  ";

        for (int i = start; i <= end; i++)
        {
            cout<<arr[i]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;
   }
   
}
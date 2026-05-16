/*
My Solution

#include <stdio.h>
void printSubarray(int arr[],int startIndex, int endIndex){
    for (int i = startIndex; i < endIndex; i++)
    {
        printf("%d",arr[i]);
    }
    printf("\n");
}
void numSubarrays(int size){
    size = 5;
    int prod = 1;
    int num = size;
    for (int i = 0; i < size; i++)
    {
        prod = prod*num;
        num--;
    }
    printf("%d",prod);
    
}
int main(){
    // print subarrays
    int arr[] = {1,2,3,4,5,6};
    printSubarray(arr,0,1);    
    int size = sizeof(arr)/sizeof(arr[0]);
    numSubarrays(size);
    return 0;
}

*/
// Correct solution
#include <stdio.h>
void printSubarrays(){
    //sub array is a continous part of an array
    // n = 5;
}
int length(int* arr){
    printf("%d",*arr);
    // return sizeof(arr)/sizeof(arr[0]);
}
int main(){
    // array of n =5;
    int arr[] = {1,2,3,4,5};
    //possible sub arrays:
    //1; 1,2; 1,2,3; 1,2,3,4; 1,2,3,4,5
    //2; 2,3; 2,3,4; 2,3,4,5;
    //3; 3,4; 3,4,5;
    //4; 4,5
    //5;
    int start = 1;
    int end = length(arr);
    printf("%d",end);
    return 0;
}
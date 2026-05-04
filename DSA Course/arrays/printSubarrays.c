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
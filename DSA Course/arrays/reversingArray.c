#include <stdio.h>
int main(){
    int arr[] = {1,2,3,4,5,6};
    int size = sizeof(arr)/sizeof(arr[0]);
    int defaultArr[size];
    for (int i = 0; i < size; i++)
    {
        defaultArr[i] = arr[i];
    }
    
    int idx = size-1;
    for (int i = 0; i < size; i++)
    {
        arr[idx]= defaultArr[i];
        idx--;
    }
    for (int i = 0; i < size; i++)
    {
        printf("%d\n",arr[i]);
    }
    
    return 0;
}
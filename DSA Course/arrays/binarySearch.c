#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}
int binSearch(int arr[],int size,int key){
    // Performing Binary Search
    int start = 0;
    int end = size - 1;
    while (start<=end)
    {
        int mid = (start+end)/2;

        if (arr[mid]==key)
        {
            return mid;
        }
        else if(arr[mid]<key){
            start = (mid)+1;
        }
        else if(arr[mid]>key){
            end = (mid) - 1;
        }

    }
    return -1;
}

int main(){
    // Binary search algorithm is a searching algorithm used for searching in a Array it is a better way than the linear search. It is only applicable for sorted arrays.

    //1. array :
    int arr[] = {2,3,53,23,92,23,32,94};
    int size = sizeof(arr)/sizeof(arr[0]);

    // Key(value to search for)
    int key = 23;
    //2. sorting the array using qsort
    qsort(arr,size,sizeof(int),compare);
    for (int i = 0; i < size; i++)
    {
        printf("%d, ",arr[i]);
    }
    printf("Found at : %d",binSearch(arr,size,key));
    return 0;
}
#include <stdio.h>
int main(){
    int key = 3;
    int arr[]= {2,56,23,32,3};
    int size = sizeof(arr)/sizeof(arr[0]);
    for (int i = 0; i < size; i++)
    {
        if (arr[i]==key)
        {
            printf("The Key is Present in %dth Place",i);
        }
        else{
            printf("Key doesn't exist");
        }
    }
    

    
    printf("\n");
    return 0;
}
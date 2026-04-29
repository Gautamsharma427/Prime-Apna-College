#include <stdio.h>

int main(){
    //=============
    int n;
    printf("Enter the Number of Elements");
    scanf("%d",&n);    

    int arr[5];
    for (int i = 0; i < n; i++)
    {
        scanf("%d",&arr[i]);
    }
    //[1,2,3,4,5]
    int largest = arr[0];
    for (int i = 0; i < n; i++)
    {
        if(arr[i]>largest){
            largest = arr[i];
        }
    }
    
    printf("%d",largest);
    //==============
    printf("\n");
    return 0;
}
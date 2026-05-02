// array pointer acts like a constant pointer 
#include <stdio.h>
int main(){
    int a = 5;
    int* ptr = &a;
    printf("%p",ptr);
    int b = 2;
    ptr = &b;
    printf("%p",ptr);
    // normal pointers like the above one aren't constant and can be changed but the array pointers cannot be changed like in example below:
    
    int arr[6];
    printf("%p",arr);//this is pointing to 0th element of the array
    b = 3;
    //arr = &b;// This would give a error as arrays pointers are read only values and cannot be modified
    return 0;
}
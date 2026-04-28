#include <stdio.h>
#include <stdlib.h>

int main(){
    // a array is a linear collection of same type of elements.
    int a[] = {1,2,3,4};
    int size = sizeof(a)/sizeof(a[0]);
    printf("%d",size);
    //Iternating over a array
    for(int i = 0;i<size;i++){
        printf("Hello World %d",a[i]);
    }
    
}
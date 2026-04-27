#include <stdio.h>

int main(){
    int a = 0;
    int *a_address = &a;
    printf("%d is located at %d",a,*a_address);
    *a_address = 1;
    int ** a_a_address = &a_address;
    printf("%d",a);
    printf("\n %d",a_address);
    printf("\n %d",**a_a_address);
    return 0;
}
#include <stdio.h>
int main(){
    int a = 0;
    int* nlp = NULL; // nlp is a Null pointer 
    printf("%p\n",nlp);
    //printf("%d",*nlp);// This would give a  error called segmentation fault because the compiler won't be able to reach a memory location

    nlp = &a; // null pointers can be changed at any time.
    printf("%p",nlp);//This would give address of the variable a
}
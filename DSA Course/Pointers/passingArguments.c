#include <stdio.h>
void changeA(int a){
    a = 5;
    printf("%d\n",a);// would change a locally in function into 5
}
void changeB(int* b){
    printf("%d\n",*b);//this will give us value of b in main function.
    *b = 56;//changing the value of b through the pointer.

}
int main(){
    int a = 0;
    changeA(a);
    printf("%d\n",a);// would still give 0
    //this method is called pass by value

    // in the second method you'll use a pointer to change the actual value and instead of passing the variable you'll pass its address and then access its address through a pointer in the other function which will change the actual variable in the main function.
    int b = 2;
    changeB(&b);
    printf("%d\n",b);// now this will give 56 because the root main variable got changed by accessing its address through the pointer.
    // This method is called pass by reference

    // The * here is called de referencing operator.


}
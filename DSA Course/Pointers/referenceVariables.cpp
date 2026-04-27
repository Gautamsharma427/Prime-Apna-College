#include <iostream>
using namespace std;
void changeC(int &c){
    c = 0;
    cout<<"The value is "<<c;

}
int main(){
    // There is another method of pass by reference which is called Reference variables but this one is only valid in c++ and not in c:- 

    int c = 32;
    changeC(c);
    cout<<"The Value outside the variable is "<<c;
    return 0;
    // so it also changed the value in here which is why we call it reference variable call. 
}
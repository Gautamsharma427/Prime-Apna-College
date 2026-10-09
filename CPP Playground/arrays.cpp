// This file contains code about the arrays
#include <iostream>
using namespace std;
int largest(int arr[],int size);

int main(){
    int arr[] = {1,2,3,4,5,23,32,109,28};
    int size = sizeof(arr)/sizeof(arr[0]);
    cout<<largest(arr,size);// should return the largest value of the array

    return 0;
}
int largest(int arr[],int size){
    int largest = arr[0];
    // get the largest value from a array
    for (int i = 0; i < size; i++)
    {
        if(arr[i]>largest){
            largest = arr[i];
        }

    }
    
    
    return largest;
}
// arrays are passed by reference which means if you change a array in a function the change reflects in the main function too!

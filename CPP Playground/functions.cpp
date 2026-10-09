// This file contains codes about the functions
#include <iostream>
using namespace std;

void sayHello(); // function declaration(compulsory in case of forward declaration)
int Prod(int a, int b);
void oddEven(int num);
int factorial(int n);
void primeNumber(int n);
void printPrimes(int n);
void changeA(int* ptr);
int main()
{
    // sayHello();           // function call
    // cout << Prod(2, 3);   // will print the returned value
    // oddEven(3);           // will print odd
    // cout << factorial(3); // will print 6
    // primeNumber(2);       // will print PRIME
    // printPrimes(13);      // 2 3 5 7 11 
    int a = 2030;
    printf("Original value of a is %d\n",a);
    changeA(&a);//passing address of a into the pointer.
    printf("Changed value of a is %d\n",a);
    return 0;
}

int Prod(int a, int b)
{
    return a * b;
}
void sayHello()
{ // function definition
    cout << "Say Hello";
}
void oddEven(int num)
{
    if (num % 2 == 0)
    {
        cout << "Even";
    }
    else
    {
        cout << "Odd";
    }
}
int factorial(int n)
{
    int factorial = 1;
    for (int i = n; i > 0; i--)
    {
        factorial = i * factorial;
    }
    return factorial;
}
void primeNumber(int n)
{
    int divisors = 0;
    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
        {
            divisors += 1;
        }
    }

    if (divisors > 0)
    {
        cout << "Not Prime";
    }
    else if (n == 1 || 0)
    {
        cout << "Neither Composite nor prime";
    }
    else
    {
        cout << "Prime";
    }
}
void printPrimes(int n)
{
    for (int i = 2; i <= n; i++)
    {
        bool isPrime = true;
        for (int j = 2; j < i; j++)
        {
            if (i % j == 0 && i != j)
            {
                isPrime = false;
                break;
            }
        }
        if (isPrime)
        {
            cout << i << "\n";
        }
    }
}
// Function overloading is when you declare multilple functions with the same name but with different number of parameters so when you call a function and give a certain number of arguments the compiler implicitly knows which one has these many arguments and it calls that one function only.

/*
pass by value is when you send a copy of the original variables in the main functions into the function.
pass by reference is when you send the address of the original variables and the original variables change when you do something to that address.
*/

// pass by reference example:
void changeA(int* ptr){
    *ptr = 20;// changing the value of the orignial variables using pointers.
    // &ptr will give the address of the pointer 
    // ptr will contain the address of the variable which was passed into function..

}

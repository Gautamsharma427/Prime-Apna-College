#include <stdio.h>
int main()
{
    // POINTER ARITHMETIC:Usually asked in MCQs and One Liners
    // Pointer variables arithmetic operations
    // 1.INCREMENT OR DECREMENT OPERATOR
    // PTR++ OR PTR--
    // ++PTR OR --PTR
    // In the above two cases in case of a pointer the pointer will point to 4byte difference in case of a integer pointer and 1 byte in case of a character pointer
    // Verification
    int a = 10;
    int *aptr = &a;
    printf("%p\n", aptr);
    aptr++; // adds 1 integer in case of a integer pointer(i.e. 4 bytes)
    printf("%p\n", aptr);
    char *cptr = "a";
    printf("%p\n", cptr);
    cptr++; // adds 1 character in case of a character pointer (i.e. 1 byte)
    printf("%p\n", cptr);

    // 2. Addition and Substraction of Pointer with a constant
    // In case of this the constant will be converted to bytes and then the bytes would be added or subtracted in the Integer
    // Example
    aptr + 3; // would convert 3 into bytes (1 int = 4 bytes; 3 int = 3x4 = 12 bytes) and hence 12 bytes would be added to the pointer.
    printf("%p\n", aptr);
    // Similar will be the case of Substraction.

    // 3. Two Pointer Operations : Addition and Substraction
    // - Addition b/w two pointers is not possible.
    // - Substraction among two pointers can be done only if both pointers are of same type.
    int c = 5;
    int *ptr1 = &c;
    int *ptr2 = ptr1+3;
    printf("%p\n",ptr1);
    printf("%p\n",ptr2);

    printf("%d\n",ptr2-ptr1);// would tell us how many pointers can we store b/w pointer 2 and pointer 1.


    // 4. comparision of two pointers would be possible by address.
    printf("%d",ptr1>ptr2);
    printf("%d",ptr2>ptr1);
    // 1 = True; 0 = False;
    printf("%d",ptr2 == ptr1);// would be zero
    return 0;
}
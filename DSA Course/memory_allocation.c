#include <stdio.h>
#include <stdlib.h>

int exercise()
{
    int n;
    printf("How many numbers you wanna store: ");
    scanf("%d", &n);

    int *values = malloc(sizeof(int) * n);
    if (values == NULL)
    {
        printf("Memory Allocation Failed!");
        free(values);
        return 0;
    }
    for (int i = 0; i < n; i++)
    {
        printf("Enter the Number: ");
        int num;
        scanf("%d", &num);
        values[i] = num;
    }
    printf("The List you made is:\n{");
    for (int i = 0; i < n; i++)
    {
        printf("%d,", values[i]);
    }
    printf("}");
    printf("\nDo you want to Store More?: ");
    int ans;
    scanf("%d", &ans);
    if (ans == 1)
    { // yes
        int *temp = realloc(values, 2 * (n * sizeof(int)));
        if (temp == NULL)
        {
            printf("Updation Failed!");
            free(values);
            return 0;
        }
        values = temp;
        for (int i = n; i < 2 * n; i++)
        {
            printf("Enter The Number\n");
            int ans;
            scanf("%d", &ans);
            values[i] = ans;
        }
        for (int i = 0; i < 2 * n; i++)
        {
            printf("%d, ", values[i]);
        }
        free(values);
        return 0;
    }
    // Not handling no
    else
    {
        free(values);
        return 0;
    }
}
int main()
{
    int array[] = {2, 5, 6, 7, 8, 43};
    int length_array = sizeof(array) / sizeof(array[0]);
    printf("The Size of array is %d\n", length_array);
    int *ptr = malloc((length_array + 1) * sizeof(int));
    for (int i = 0; i <= length_array; i++)
    {
        if (i < length_array)
        {
            ptr[i] = array[i];
        }
        else
        {
            scanf("%d", &ptr[i]);
        }
    }
    int length_ptr = length_array + 1;
    printf("The Following is the updated array: \n");
    for (int i = 0; i < length_ptr; i++)
    {
        printf("%d\n", ptr[i]);
    }
    free(ptr);

    // ==============================================
    printf("\n");

    exercise();
    return 0;
}

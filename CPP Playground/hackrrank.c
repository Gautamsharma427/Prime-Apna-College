#include <stdio.h>
#include <string.h>
    
// int main() {
// struct Student{
//         int rollNo;
//         char Name[30];
//         float Marks;
// };
// struct Student Gautam;

//     scanf("%d",&Gautam.rollNo);getchar();
//     fgets(Gautam.Name, sizeof(Gautam.Name),stdin);
//     scanf("%f",&Gautam.Marks);
//     printf("Roll No : %d\nName: %sMarks: %.2f",Gautam.rollNo,Gautam.Name,Gautam.Marks);
//     return 0;
//     /*
//     Roll Number: 101
//     Name: Rahul
//     Marks: 87.50
//     */
// }
struct Employee{
    int id;
    char name[51];
    float salary;
    
};
int main() {
    int num;
    scanf("%d",&num);
    struct Employee e[num];
    //2 
    for(int i = 0; i<num;i++){
        
        scanf("%d",&e[i].id);getchar();
        fgets(e[i].name, sizeof(e[i].name), stdin);
        scanf("%f",&e[i].salary);
    }
    for (int i = 0; i < num; i++)
    {
        printf("Empolyee ID: %d\n",e[i].id);
        printf("Employee Name: %s",e[i].name);
        printf("Salary: %.2f",e[i].salary);
        printf("\n");
    }
    
    return 0;
}

#include <stdio.h>
#include<math.h>
int main(void){
float num;
float type;
float numtwo;
printf("enter the first digit\n");
if(0 == scanf("%f", &num)) {
num = 0;
scanf("%*s");
}
printf("type one for addition two for subtraction\n");
printf("three for multiplication, and four for division\n");
printf("...\n");
if(0 == scanf("%f", &type)) {
type = 0;
scanf("%*s");
}
printf("what is your second number\n");
if(0 == scanf("%f", &numtwo)) {
numtwo = 0;
scanf("%*s");
}
if(type==1.0){
printf("%.2f\n", (float)(num+numtwo));
}
if(type==2.0){
printf("%.2f\n", (float)(num-numtwo));
}
if(type==3.0){
printf("%.2f\n", (float)(num*numtwo));
}
if(type==4.0){
printf("%.2f\n", (float)(num/numtwo));
}
return 0;
}

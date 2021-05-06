num1,num2=eval(input("Enter two number"))
max_number=max(num1,num2)
if(max_number==num1):
    divisor,divident=num2,num1
else:
    divisor,divident=num1,num2
remainder=divident%divisor
while(remainder!=0):
    divident,divisor=divisor,remainder
    remainder=divident%divisor
print("HCF of ", num1 ,"and",num2 , "is :",divisor)

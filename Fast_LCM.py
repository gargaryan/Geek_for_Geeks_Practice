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
HCF=divisor
# we use Num1*Num2=LCM*HCF formula to find out the LCM of Two number
LCM=int((num1*num2)/HCF)
print("LCM of ", num1,"and ",num2 ,"is: ",LCM)

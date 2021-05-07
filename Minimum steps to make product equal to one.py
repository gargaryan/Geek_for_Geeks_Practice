#Amazon Question
#Minimum step to make the product Zero
l=[-1,-5,-6,0,7,9,10]
step=0
zeroes=0
negative=0
for i in l:
    if(i==0):
        zeroes+=1
        step+=1
    elif(i>0):
        step+=(i-1)
    else:
        negative+=1
        step+=(-1-i)
if(negative%2==1 and zeroes==0):
    step+=+2
        
print(step)
        


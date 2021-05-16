#Next Greatest Element Using Stack 
arr=[13,6,7,12]
stack=[]
stack.append(0)
for i in range(1,len(arr)):
    if(len(stack)!=0):
        while(arr[stack[-1]]<arr[i]):
            arr[stack[-1]]=arr[i]
            stack.pop()
            if(len(stack)==0):
                break
        stack.append(i)
        if(arr[stack[-1]]>arr[i]):
            stack.append(i)
while(len(stack)!=0):
    arr[stack[-1]]=-1
    stack.pop()
print(arr)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Time-complexity-O(N)
#Space-Complexity-O(N)

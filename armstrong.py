print("enter the number:")
num = int(input())
sum=0
#find the sum of the cube of each digit
temp=num
while(temp>0):
 digit=temp%10
sum=sum+(digit**3)
temp//=10
# Display the result
if(num == sum):
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")



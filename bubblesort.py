# Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print("pass",i)
        print(arr)
    return arr


# Main function
EmpSalary=[]
numberofmembers=int(input("Enter total number of Employee : "))
for i in range(numberofmembers):
    Salary=float(input("Enter Salary of Employee "+str(i+1)+" : "))
    EmpSalary.append(Salary)

flag=1
while flag==1:
    print("\n\n--------------------MENU--------------------\n")
    print("1. Bubble Sort")
    print("2. Exit\n")
    ch=int(input("Enter your Choice (from 1 to 2) :"))

    if ch==1:
        bubble_sort(EmpSalary)
        print("Sorted Salary using Bubble Sort: ",EmpSalary)
        a = input("Do you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==2:
        flag=0
        print("Thanks for using this program!")

    else:
        print("!!Wrong Choice!! ")
        a=input("Do you want to continue (yes/no) :")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Thanks for using this program!")

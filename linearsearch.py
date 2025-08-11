 # linear search
def linearsearch(arr, n, key):
    found = False
    for i in range(n):
        if arr[i] == key:
            print("Customer ID Found at index", i)
            found = True
            break
    if not found:
        print("Customer ID NOT Found in list")

# main function
CustomerID = []
numberofmember = int(input("Enter total number of Customers: "))
for i in range(numberofmember):
    ID = int(input("Enter Customer ID of member " + str(i + 1) + ": "))
    CustomerID.append(ID)

flag = 1
while flag == 1:
    print("\n\n____________MENU___________\n")
    print("1. Linear Search")
    print("2. Exit\n")
    ch = int(input("Enter your choice (from 1 to 2): "))

    if ch == 1:
        key = int(input("Enter Customer ID to be searched: "))
        linearsearch(CustomerID, numberofmember, key)
        a = input("Do you want to continue (yes/no): ")
        if a.lower() == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch == 2:
        flag = 0
        print("Thanks for using this program!")

    else:
        print("!!Wrong Choice!!")
        a = input("Do you want to continue (yes/no): ")
        if a.lower() == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")
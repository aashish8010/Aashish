  # Binary Search    
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

# Main function
CustomerID = []
numberofmembers = int(input("Enter total number of Customers : "))
for i in range(numberofmembers):
    ID = int(input("Enter Customer ID of Member " + str(i + 1) + " : "))
    CustomerID.append(ID)

flag = 1
while flag == 1:
    print("\n\n--------------------MENU--------------------\n")
    print("1. Binary Search")
    print("2. Exit\n")
    ch = int(input("Enter your Choice (from 1 to 2) :"))

    if ch == 1:
        CustomerID.sort()
        key = int(input("Enter Customer ID to be searched: "))
        result = binary_search(CustomerID, 0, numberofmembers - 1, key)
        if result != -1:
            print("Customer ID is present at index", str(result))
        else:
            print("Customer ID is not present in array")
        a = input("Do you want to continue (yes/no) :")
        if a.lower() == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch == 2:
        flag = 0
        print("Thanks for using this program!")

    else:
        print("!!Wrong Choice!! ")
        a = input("Do you want to continue (yes/no) :")
        if a.lower() == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")



 
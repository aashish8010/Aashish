 # Compute the average number of books borrowed by all library members
def average(listofbookborrow):
    total = 0
    count = 0
    for val in listofbookborrow:
        total += val
        count += 1
    avg = total / count if count != 0 else 0
    print("Total number of books borrowed: ", total)
    print("Average number of books borrowed: {:.2f}".format(avg))


# Find the book with the highest number of borrowings in the library
def Maximum(listofbookborrow):
    max_val = listofbookborrow[0]
    for val in listofbookborrow:
        if val > max_val:
            max_val = val
    return max_val


# Find the book with the lowest number of borrowings in the library
def Minimum(listofbookborrow):
    min_val = listofbookborrow[0]
    for val in listofbookborrow:
        if val < min_val:
            min_val = val
    return min_val


# Count the number of members who have not borrowed any books
def notBorrow(listofbookborrow):
    count = 0
    for val in listofbookborrow:
        if val == 0:
            count += 1
    return count


# Display the most frequently borrowed book
def maxFrequency(listofbookborrow):
    frequency = {}
    for book in listofbookborrow:
        frequency[book] = frequency.get(book, 0) + 1

    print("Books  |  Frequency")
    for book, freq in frequency.items():
        print(f"{book}     |  {freq}")

    max_book = max(frequency, key=frequency.get)
    return max_book, frequency[max_book]


# Main function
bookBorrow = []
numberofmembers = int(input("Enter total number of Library Members: "))
for i in range(numberofmembers):
    book = int(input("Enter number of books borrowed by Member " + str(i + 1) + ": "))
    bookBorrow.append(book)

flag = 1
while flag == 1:
    print("\n\n--------------------MENU--------------------\n")
    print("1. Total and Average number of books borrowed by all library members")
    print("2. Book with the highest and lowest number of borrowings in the library")
    print("3. Count the number of members who have not borrowed any books")
    print("4. Display the most frequently borrowed book")
    print("5. Exit\n")
    ch = int(input("Enter your Choice (from 1 to 5): "))

    if ch == 1:
        average(bookBorrow)

    elif ch == 2:
        print("Highest number of books borrowed by a member: ", Maximum(bookBorrow))
        print("Lowest number of books borrowed by a member: ", Minimum(bookBorrow))

    elif ch == 3:
        print("Number of members who have not borrowed any books: ", notBorrow(bookBorrow))

    elif ch == 4:
        book, freq = maxFrequency(bookBorrow)
        print(f"Most frequently borrowed value is {book} with a frequency of {freq}")

    elif ch == 5:
        print("Thanks for using this program!")
        break

    else:
        print("!!Wrong Choice!!")

    a = input("Do you want to continue (yes/no): ").strip().lower()
    if a != "yes":
        flag = 0
        print("Thanks for using this program!")
# Input book names available in library
books = ["A", "B", "C", "D", "E", "F", "G"]
print("NAME OF BOOKS AVAILABLE:", books)
print("NUMBER OF BOOKS AVAILABLE:", len(books))

# Input number of members
number_of_members = int(input("\nEnter total number of library members: "))
member_borrow_counts = []
member_borrowed_books = []

# Input borrow details from each member
for i in range(number_of_members):
    print(f"\n--- Member {i+1} ---")
    count = int(input(f"Enter number of books borrowed by Member {i+1}: "))
    member_borrow_counts.append(count)
   
    if count > 0:
        book_names = input(f"Enter names of {count} book(s) borrowed by Member {i+1} (comma separated): ").split(',')
        member_borrowed_books.extend([book.strip() for book in book_names])
    else:
        print("No books borrowed.")

# MENU FUNCTIONS

def total_and_average_borrowed():
    total = sum(member_borrow_counts)
    avg = total / number_of_members if number_of_members else 0
    print(f"\nTotal number of books borrowed: {total}")
    print("Average number of books borrowed: {:.2f}".format(avg))

def highest_lowest_borrow_count():
    if member_borrow_counts:
        print("\nHighest borrow count by a member:", max(member_borrow_counts))
        print("Lowest borrow count by a member:", min(member_borrow_counts))
    else:
        print("No borrowing data available.")

def count_non_borrowers():
    count = member_borrow_counts.count(0)
    print(f"\nNumber of members who have not borrowed any books: {count}")

def most_frequent_books():
    if member_borrowed_books:
        book_counts = Counter(member_borrowed_books)
        max_freq = max(book_counts.values())
        most_borrowed = [book for book, count in book_counts.items() if count == max_freq]
        print("\nMost frequently borrowed book(s):", most_borrowed)
        print("Frequency of most borrowed book(s):", max_freq)
    else:
        print("No books have been borrowed yet.")

# MAIN MENU LOOP
while True:
    print("\n-------------------- MENU --------------------")
    print("1. Total and Average number of books borrowed")
    print("2. Highest and Lowest borrow count by members")
    print("3. Number of members with no borrowed books")
    print("4. Most frequently borrowed book(s)")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == '1':
        total_and_average_borrowed()
    elif choice == '2':
        highest_lowest_borrow_count()
    elif choice == '3':
        count_non_borrowers()
    elif choice == '4':
        most_frequent_books()
    elif choice == '5':
        print("Thanks for using the library system!")
        break
    else:
        print("Invalid choice! Please select a valid option.")

    cont = input("\nDo you want to continue? (yes/no): ").lower()
    if cont != "yes":
        print("Thanks for using the library system!")
        break

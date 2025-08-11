#accepting the numbers of elements
N = int(input("enter the numbers of elements:"))
#create an empty list to store the numbers
numbers = []
#acepting N empty from user
for i in range(N):
    num = float(input(f"enter numbers{i+1}:"))
    numbers.append(num)
#caculating the maximum,minimum,sum
max_num = max(numbers)
min_num= min(numbers)
# displaying the results
print("\nresults")
print(f"maximum:{max_num}")
print(f"minimum:{min_num}")



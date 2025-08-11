import statistics
#library management
borrow_counts=[2,0,3,5,0,2]
book_borrow_counts={'Book1':4,'Book2':1,'Book3':7}

#avg num of books borrowed
sumofbook=0
for i in range(len(borrow_counts)):
    
     sumofbook=sumofbook + borrow_counts[i]
     

avg=sumofbook/len(borrow_counts)
print("avg num of books borrowed is:",avg)

#highest and lowest book borrowed
maxbook=0
minbook=0
listofbook=book_borrow_counts.values()
maxbook=max(listofbook)
minbook=min(listofbook)
print("max num of book:",maxbook,max(book_borrow_counts))
print("min num of book:",minbook,min(book_borrow_counts))

#members with zero book borrowed
count=0
for i in borrow_counts:
      if i==0:
          count+=1
print("member with zero book borrowed:",count)

#mode of borrowed book
print("mode is:",statistics.mode(borrow_counts))


#OUTPUT
#[Running] python -u "c:\Users\Shree\Desktop\CS corner\python\library.py"
#avg num of books borrowed is: 2.0
#max num of book: 7 Book3
#min num of book: 1 Book1
#member with zero book borrowed: 2
#mode is: 2

#[Done] exited with code=0 in 2.412 seconds
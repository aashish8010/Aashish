# calculate to salary of employ
basic_pay = int(4000)
print("basic pay =", basic_pay)
HRA = (10*basic_pay)/100
print("HRA =",HRA)
TA = (5*basic_pay)/100
print("TA =",TA)
total_salary =basic_pay + HRA + TA
print("total salary =",total_salary)
profestional_tax = (2*total_salary)/100
print("profestional tax =", profestional_tax)
net_salary = total_salary - profestional_tax
print("net salary =", net_salary)
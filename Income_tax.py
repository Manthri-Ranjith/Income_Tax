#writing the program using python for the employee have to pay tax to the government
#Enter the salalry of an employee of his month earnings
count=int(input("How many employees are there:"))
#The compiler take from the user that how many employees are there and adding to the loop
def tax():
#User defined function and naming it as tax i.e.Function decleration.
    print("INCOME-TAX")
    print("Enter the salary of an employee")
    jan=int(input("January:"))
    feb=int(input("February:"))
    mar=int(input("March:"))
    apr=int(input("April:"))
    may=int(input("May:"))
    jun=int(input("June:"))
    july=int(input("July:"))
    aug=int(input("August:"))
    sep=int(input("September:"))
    octem=int(input("October:"))
    nov=int(input("November:"))
    dec=int(input("December:"))
    
    total=jan+feb+mar+apr+may+jun+july+aug+sep+octem+nov+dec
    
#caliculating the sum of salary of an employee per anum i.e. per year.
#Because we have to pay tax to the govrenment of salary

    if total>=1500000:
#If the total amount per anum which is more than fifteen lakhs
#The person have to pay 30% of tax from the total amount
        amt=30*total/100
#Caliculating the tax amount of 30% from the total amount
        print("The tax which we have to pay for the government:",amt)
#printing the tax amount person have to pay for the government
    
    elif total>=1200000:
#If the total amount per anum is greater than 1200000 then the preson have to pay 20% of tax
# from the total amount

        amt=20*total/100
#caliculating the 20% tax from the total amount per anum
        print("The tax which we have to pay for the government is:",amt)
#Printing the tax amount which the preson have to pay of his earinigs
    
    elif total>=1000000:
#If the total amount is greater than the ten lakhs then the preson have to pay the 15% of tax
#from the total amount
        amt=15*total/100
        print("The tax which we have to pay for the government is:",amt)
    
    elif total>=700000:
#If the amount is greater than the seven lakhs then the preson have to pay 10%
#of tax from the total amount
        
        amt=10*total/100
        print("The tax which we have to pay for the government is:",amt)
    
    elif total>=300000:
#If the amount is greater than three lakhs then the preson have to pay the 5% 
#of tax from the total amount
        amt=5*total/100
        print("The tax which we have to pay for the government is:",amt)
    
    else:
        print("No tax is required")
#If the preson earnings is less then three lakhs then no tax is required
        amt=0
    
    final_amt=total-amt
#Subtracting  the tax amount from the total amount per anum

    print("The final amount in your bank account is:",final_amt)
#The final amount which is there in your account will be displayed
tax()
#closing the function tax function
i=count
while i>0:
    
# I used while loop which is also called the jumping loop
    tax()
#calling the tax function that how many employees are there
i=i-1




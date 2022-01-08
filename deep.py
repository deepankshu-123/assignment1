#question 1
first_number=int(input("Enter the first number "))
second_number=int(input("Enter the second number "))
third_number=int(input("Enter the third number "))
print("The average is:",(first_number + second_number + third_number)/3)


#question 2
total_income=int(input("Enter your total income (in $) "))
standard_deduction= 10000
no_of_dependents=int(input("Enter the number of dependents "))
taxable_income=total_income-standard_deduction-(3000*no_of_dependents)
print("tax that you are paying consists of 20% of your taxable income,Tax that you need to pay is: ",taxable_income*0.2)

#question 3
list1=[21104013,"Deepankshu gautam",'F',"intro to computing",9.8]
print("The list is: ",list1)

#question 4
first=input("Enter the marks of first student ")
second=input("Enter the marks of second student ")
third=input("Enter the marks of third student ")
fourth=input("Enter the marks of fourth student ")
fifth=input("Enter the marks of fifth student ")
list2=[first,second,third,fourth,fifth]
list2.sort()
print("The sorted list of marks of above students is as follows: ",list2)

#question 5 (a)
list_of_colors=["Red","Green","White","Black","Pink","Yellow"]
list_of_colors.remove("Black")
print(list_of_colors)

#question 5(b)
list_of_colors=["Red","Green","White","Black","Pink","Yellow"]
list_of_colors.remove("Pink")
list_of_colors.remove("Black")
list_of_colors.insert(3,"Purple")
print(list_of_colors)

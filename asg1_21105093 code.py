#ASSIGNMENT 1 (SID->21105093)
print('OUTPUT 1')
print(' ')


#program 1->TO FIND AVERAGE OF THREE NUMBERS


num1=int(input('enter first number :'))
num2=int(input('enter second number :'))
num3=int(input('enter third number :'))
avg=(num1+num2+num3)/3
print('average of three numbers added by user is :',avg)


#END


print(' ')
print(' ')
print('OUTPUT 2')
print(' ')


#program 2->TO COMPUTE A PRESON'S INCOME TAX


income=float(input('Enter your gross income: '))
no_of_dep=int(input('Input the number of Dependents: '))          
ded=10000                                      
ded_per_dep=3000                                                                      
taxable_inc=income-ded-(ded_per_dep*no_of_dep)
tax=float()                                   
tax=taxable_inc*(20/100)
print('Your total income tax is: ',tax)


#END


print(' ')
print(' ')
print('OUTPUT 3')
print(' ')


#program 3->TO STORE DIFFRENT DATA TYPE VALUES IN TO A LIST


print('Student Information->[SID, Name, Gender, Course Name, CGPA]')
student=[21105093,'AkshatDutta','M','ECE',9.2]
print(student)


#END


print(' ')
print(' ')
print('OUTPUT 4')
print(' ')


#program 4->TO DISPLAY MARKS OF FIVE STUDENTS IN SORTED MANNER


print('given marks of five students')
marks=[77,80,93,85,90]
print(marks)
print('marks of students in sorted manner')
marks.sort()
print(marks)


#END


print(' ')
print(' ')
print('OUTPUT 5a')
print(' ')


#program 5a->TO REMOVE 4TH ELEMENT IN THE LIST(i.e 'Black')


color=['Red','Green','White','Black','Pink','Yellow']
print('given list ->',color)
color.pop(3)
print('list after removing black from it ->',color)


#END


print(' ')
print(' ')
print('OUTPUT 5b')
print(' ')


#program 5b->TO REMOVE 'BLACK' AND 'PINK' FROM THE LIST AND REPLACE WITH 'PURPLE'
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print('given list ->',color)
print('list after replacing Black and Pink and inserting purple->')
color[3:5] = ['purple']
print(color)


#END











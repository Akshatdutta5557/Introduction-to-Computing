print('\tASSIGNMENT3\n')

print('\tQ1\n')


string=str(input('enter a string: '))
#using .lower() function so that 'The' = 'the' 
string=string.lower()
#creating dictionary to store the result
dict1={}
dict2={}
#using condition to distinguish a word and a line
if ' ' not in string :
#this loop will execute if user enters only a word      
     list_of_letters=list(string)
     for letter in list_of_letters :
         if letter in dict1 :
             dict1[letter]+=1
         else :
             dict1.update({letter:1})
     print('the string entered is a word \nnumber of each letter in string is',dict1)        
else :
    list_of_words=string.split(' ')
    for word in list_of_words :
        if word in dict2 :
            dict2[word]+=1
        else :
            dict2.update({word:1})
    print('the number of each word in entered string is',dict2)


#############################################################################################################################################################


print('\tQ2\n')


import sys
date=int(input('enter date: '))
month=int(input('enter month: '))
year=int(input('enter year: '))
#checking if date meets the given question conditions
if (1<=month<=12) and (1<=date<=31) and (1800<=year<=2025): 
#finding next date for months with 30 days
    if month in (4,6,9,11) :
        if date<30 :
            date+=1
        else :
            date=1
            month+=1
#finding next date for months with 31 days
    elif month in (1,3,5,7,8,10) :
        if date<31 :
            date+=1
        else :
            date=1
            month+=1
#finding next date for feburary
    elif month==2 :
#finding next date for leap year
        if (year%4)==0 :
            if date<29 :
                date+=1
            elif date>29 :
                sys.exit('invalid date for feb')
            else :
                date=1
                month+=1
        else :
            if date<28 :
                date+=1
            elif date>28 :
                sys.exit('invalid date for feb')
            else :
                date=1
                month+=1
#finding next date for december
    else  :
        if date<31:
            date+=1
        else :
            date=1
            month=1
            year+=1
#printing output
    print(f'Next day is: {date}/{month}/{year}')
else:
    print('invalid Date')


#############################################################################################################################################################


print('\tQ3\n')


list1=[]
list2=[]
n=int(input("Enter number of elements : "))
for i in range(0,n):
    element=int(input('enter number'))
    list1.append(element)
for a in list1 :
    tuple1=(a,a*a)
    list2.append(tuple1)
print(list2)


#############################################################################################################################################################


print('\tQ4\n')


#using nested loop
grade_point=int(input("Enter the grade point: "))
if 4<=grade_point<=10 :
    if grade_point==10:
        print("Your grade is 'A+' and Outstanding Performance.")
    elif grade_point==9:
        print("Your grade is 'A' and Excellent Performance.")
    elif grade_point==8:
        print("Your grade is 'B+' and Very Good Performance.")
    elif grade_point==7:
        print("Your grade is 'B' and Good Performance.")
    elif grade_point==6:
        print("Your grade is 'C+' and Average Performance.")
    elif grade_point==5:
        print("Your grade is 'C' and Below Average Performance.")
    else:
        print("Your grade is 'D' and Poor Performance.")
else:
    print("Invalid grade.")


#############################################################################################################################################################


print('\tQ5\n')


letters=['A','B','C','D','E','F','G','H','I','J','K']
a=1
while a<=6 :
    for i in letters :
        print(i, end="")
    letters.pop(len(letters)-1)  
    letters.pop(len(letters)-1)  
    letters.insert(0, " ")
    print()
    a+=1


#############################################################################################################################################################


print('\tQ6\n')


dict1={}
x=True
a='Y'
#using while loop to repeatedly ask user for sid and name
while x==True :
    if  a=='Y' or a=='y' :
        sid=int(input('enter SID : '))
        name=str(input('enter name : '))
        dict1[sid]=name
        print('to cotinue type y else press n')
        a=str(input())
        x=True
    else :
        x=False

print('A part')
print('student details are in the format {sid: name} ')
print(dict1)

print('B part')
name_sort=sorted(dict1.values())
list_of_names=list(dict1.values())
list_of_sid=list(dict1.keys())
sorted_dict_by_names={}
print('Sorted dictionary using student names : ')
for name in name_sort :
    for i in range(len(list_of_names)) :
        if list_of_names[i]==name :
            sorted_dict_by_names.update({list_of_sid[i] : name})
print('Sorted dictionary by names is : ',sorted_dict_by_names)

print('C part')
sorted_dict_by_sid=dict(sorted(dict1.items()))
print('Sorted dictionary using sid : ',sorted_dict_by_sid)

print('D part')
search_sid=int(input('enter sid for student name :'))
found_name=dict1.get(search_sid)
print(found_name)


#############################################################################################################################################################


print('\tQ7\n')


#taking help of recursion function
def fibonacci(n):
    if n<=1:
       return n
    return(fibonacci(n-1) + fibonacci(n-2))
count=0
sum=0
while True :
    n=int(input('enter a positive integer: '))
    if n>0 :
        print('fibonacci sequence with ',n,'terms: ')
        for i in range(n) :
            sequence=fibonacci(i)
            print(sequence)
            sum+=sequence
            count+=1
        break
    else :
        print('enter a valid positive integer')
print('average of fibonacci sequence is: ',(sum/count))


#############################################################################################################################################################


print('\tQ8\n')


set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

print('A part')
setA=(set1|set2)-(set1&set2)
print('set of all elements that are in Set1 and Set2 but not both: ',setA)

print('B part')
setB=(set1 | set2 | set3)-(set1 & set2 & set3)-(set2 & set3)-(set3 & set1)-(set2 & set1)
print('set of all elements that are in only one of the three sets Set1,Set2 and Set3',setB)

print('C part')
setC=((set1 & set2) | (set2 & set3) | (set1 & set3))-(set1 & set2 & set3)
print('set of elements that are exactly two of the sets Set1, Set2and Set3: ',setC)

print('D part')
setD={1,2,3,4,5,6,7,8,9,10} - set1
print('set of all integers in the range 1 to 10 that are not in Set1: ',setD)

print('E part')
setE={1,2,3,4,5,6,7,8,9,10} - set1 - set2 - set3
print('new set of all integers in the range 1 to 10 that are not in Set1,Set2 and Set3: ',setE)


#############################################################################################################################################################
        






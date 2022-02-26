print('\t\tASSIGNMENT 4\n\n')
print('\t\tQUESTION 1\n\n')


#taking 3 disks : disk1, disk2, disk3
#3 rods : rod A, rod B, rod C
#considering 3 disks are in rod A
#we have to shift disks to rod B 
def tower_of_hanoi(n, rodA, rodB, rodC):
   if n==1:
      print("move disk 1 from rod",rodA,"to rod",rodB)
      return 
   tower_of_hanoi(n-1, rodA, rodC, rodB)
   print("move disk",n,"from rod",rodA,"to rod",rodB)
   tower_of_hanoi(n-1, rodC, rodB, rodA)
n=3
tower_of_hanoi(n,'A','B','C')

print('\n\n')
############################################################################
print('\t\tQUESTION 2\n\n')


n=int(input("enter number of rows for Pascal's Triangle: "))

print("\tpascal's triangle using recursions\n")

def pascal(n, m=n):
    if n == 0:
        return
    pascal(n-1,m)
    print('  '*(m-n), end='')
    number=1
    for i in range(1, n+1):
        print(number, end ='   ')
        number=number*(n-i) // i
    print()
pascal(n)


print("\tpascal's triangle using iterations\n")

for lines in range(1, n+1):
    print('  '*(n - lines), end='')
    number= 1
    for i in range(1, lines+1):
        print(number, end='   ')
        number=number*(lines-i) // i
    print()

print('\n\n')
############################################################################
print('\t\tQUESTION 3\n\n')


a=int(input("enter a integer: "))
b=int(input("enter another integer(not zero): "))
#using inbuilt function divmod()
quo_rem=divmod(a,b)
#divmod() stores values in a tuple
print(f'the quotient and reminder of {a} and {b} is {quo_rem}')


#a part-checking if callable
#using inbuilt function callable()
print('\t\tA PART')

x=callable(quo_rem)
if(x==True):
    print('CALLABLE')
else:
    print('NOT CALLABLE')
    

#b part-checking if all nonzero or not
#using inbuilt function all()
print('\t\tB PART')

if(all(i==0 for i in quo_rem)):
    print('all are 0')
else:
    print('not all 0')


#c part-adding (4,5,6) and finding values > 4
#usin inbuilt function __add__()
print('\t\tC PART')

new_tuple=quo_rem.__add__((4,5,6))
print('new tuple after adding (4,5,6) to it: ',new_tuple)
greater_than_four=[]
for i in range(len(new_tuple)):
    if new_tuple[i] > 4:
        greater_than_four.append(new_tuple[i])
print('values greter than 4 are: ',greater_than_four)


#d part-converting new tuple into set
#using inbuilt function set()
print('\t\tD PART')

new_set=set(new_tuple)
print('converting new tuple into set: ',new_set)


#e part-making the set immutable
#usin inbuilt function frozenset(), it makes set immutable
print('\t\tE PART')

immutable_set=frozenset(new_set)
print(f'now {immutable_set} is immutable')


#f part-finding maximum value from set and its hash value
#usin inbuilt functions max() and hash()
print('\t\tF PART')

max_value=max(immutable_set)
hash_value=hash(immutable_set)
print(f'maximum value from set is {max_value} \nits hash value is {hash_value}')

print('\n\n')
############################################################################
print('\t\tQUESTION 4\n\n')


class Student():
    #using _init_() function to assign values for name and roll number
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        print(f'name of student: {self.name} \nrollno. of student: {self.rollno}')

    def __del__(self):
        print(f'object deleted for student {self.name}')
    
#object creation
student1=Student('Akshat dutta',21105093)
student2=Student('Ayush kher',21105001)
student3=Student('Armeen singh',21105002)
#object destruction
del student1
del student2
del student3

print('\n\n')
############################################################################
print('\t\tQUESTION 5\n\n')


class Employee():
    #using init function to store details
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    #function for updating salary
    def salary_update(self,new_salary):
        
        print(f"{self.name}'s salary is updated from {self.salary} to {new_salary}")
        self.salary=new_salary

    #destructor for deleting employee record
    def __del__(self):
        print(f'record of {self.name} is deleted.')
    
#object creation
object1=Employee('Mehak',40000)
object2=Employee('Ashok',50000)
object3=Employee('Viren',60000)

#part a-updating mehak's salary
object1.salary_update(70000)

#part b-deleting viren's record
del object3

print('\n\n')
############################################################################
print('\t\tQUESTION 6\n\n')


word1=str(input('enter your first word: '))
word2=str(input('enter a new word with same letters to test you friendship: '))
def counting_letters(word):
    dict1={}
    list_of_letters=list(word)
    for letter in list_of_letters :
        if letter in dict1 :
            dict1[letter]+=1
        else :
            dict1.update({letter:1})
    return dict1
if (counting_letters(word1) != counting_letters(word2)):
    print('friendship is fake')
else:
    print('true friendship')

print('\n\n')
############################################################################
print('\t\tASSIGNMENT OVER\n\n')






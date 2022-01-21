print('Q1\n')

string='Python is a case sensitive language'

# finding the length of string
print("Part a")
print('Length of Input String =',len(string))

# printing the string in reverse order
print("\nPart b")
print(string[::-1])

# using slice function on string
print("\nPart c")
sliced_string=string[10:26]
print(sliced_string)

# replacing and printing
print("\nPart d")
new_string=string.replace("a case sensitive", "object oriented")
print(new_string)

# finding index of "a" in string
print("\nPart e")
print(string.index("a"))

# removing white spaces
print("\nPart f")
print(string.replace(" ",""))


#end of question 1


print("Question 2\n")


name="Akshat Dutta"
SID=21105093
dept="ECE"
CGPA=9.5
print('Hey, %s' %(name),'Here!\nMy SID is %i'%(SID),'\nI am from %s'%(dept),'department and my CGPA is %f'%(CGPA))
      

#end of question 2


print("Question 3\n")


a = 56
b = 10
print("(a)a&b is = ",a&b)
print("(b)a|b is =",a|b)
print("(c)a^b is =",a^b)
print("(d)Left shifting a and b with 2 bits->\na<<2 : ", a << 2, "\tb<<2 :", b << 2)
print("(e)Right shifting a and b with 2 bits->\na>>2 : ", a >> 2, "\tb>>2 :", b >> 4)


#end of question 3


print("Question 4")

a=int(input("give first number"))
b=int(input("give second number"))
c=int(input("give third number"))
if a>b:
    if a>c:
        highest_no=a
    else:
        highest_no=c
if b>a:
    if b>c:
        highest_no=b
    else:
        highest_no=c
print("Highest number=",highest_no)


#end of question 4


print("Qustion 5")

string=input("Input a string")
if "name" in string:
    print("Yes")
else:
    print("No")


#end of question 5


print("Question 6\n")

a=int(input("Enter 1st length")) 
b=int(input("Enter 2nd length"))
c=int(input("Enter 3rd length"))
if a+b>c and a+c>b and b+c>a:
    print("Yes")
else:
    print("No")

#end of question 6    

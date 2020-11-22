#Constants - fixed values
#To denote strings we use ' ', " "
print(98.6)
print('Hello')

#Reserved Words else, int ,float
#Variables 
x=12 # X is a variable that stores 12 in memory 
print(x)#Function call
x=13
print(x)#The value of X is OverWritten

#Python 3 will return float value in division operator(/)
u=8/4
print(u)

#Follow the Order of Evaluation (), **, * or /(L to R), + or - (L to R), Left to Right
x=3.9*x*1-x 
print(x)
y=1+2**3/4*5 #1. 2**3=8 , 2. 8/4=2 (L to R), 3. 2*5=10, 4. 10+1=11
print(y)

#Type Function
var='Hello'
type(x)
type(var)
#print(x+var) Type error because string cannot be added to int

#Type Conversations
i=48 #Assigned i to int
print(float(i))
j='52'
print(int(j)+i) #Converted string 52 to int and added it to i
j='Hello'
#print(int(j)) Valuee Error because Hello is a string type and cannot be converted

#User Input
char=input('Type Hello')
print(char)
name=input('Is it even?')
print(name) #Python will Take both the user inputs

#Always Remember THE USER INPUT WILL BE STRING TYPE
age=input('Whats your age?')
print('Age = ',age)
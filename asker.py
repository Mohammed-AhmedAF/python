name = input("Enter your name: ")
age = input("Enter your age: ")
try :
	age = int(age)
except :
	age = -1

print("Your age is "+ str(age))

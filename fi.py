largest = None
smallest = None 


while True:
	num = input("Enter a number: ")
	if(num == "done"):
		break
	try:
		x = int(num)
	except:
		print("Invalid input")
		continue
	else :
		if (smallest is None) & (largest is None):
			smallest = x
			largest = x
		elif x < smallest:
			smallest = x
		if x > largest:
			largest = x
	
print("Maximum", largest)
print("Minimum", smallest)

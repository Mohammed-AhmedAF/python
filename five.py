largest = None
smallest = None
while True:
    num = input("Enter a number: ")
	if num == "done" :
		break
	try :
		num = int(num)
	if num > largest:
        	largest = num
	if num < smallest:
		smallest = num
    except :
            print("Error")
        print(num)

print("Maximum", largest)

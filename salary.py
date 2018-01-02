def computePay(hours, rate):
	if hours > 40:
		return (hours-40)*rate*1.5+40*rate
	else :
		return hours*rate

hours = input("Enter hours: ")
rate = input("Enter rate: ")

h = float(hours)
r = float(rate)

salary = computePay(h,r)
print("Salary: " + str(salary))



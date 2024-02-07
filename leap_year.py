# Nested Conditional Method

year = input("Enter a year: ")
year = int(year)

if year % 4== 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print(year, "is a leap year!")
		else:
			print(year, " is not a leap year")
	else:
		print(year, " is a leap year")
else:
	print(year, " is not a leap year")

# Long Conditional Method

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
	print(year, " is a leap year")
elif year % 4 == 0 and year % 100 == 0:
	print(year, " is not a leap year")
elif year % 4 == 0:
	print(year, " is a leap year")
else:
	print(year, " is not a leap year")



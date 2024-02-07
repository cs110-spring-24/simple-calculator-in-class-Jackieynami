num1 = int(input("Enter your num 1: "))
op = input("Enter your operator: ")
num2 = int(input("Enter your num 2: "))

elif op == "+":
	total = num1 + num2
	print(f"{num1} + {num2} = {total}")

elif op == "-":
	total = num1 - num2
	print(f"{num1} - {num2} = {num1 - num2}")

elif op == "*":
	total = num1 * num2
	print(f"{num1} * {num2} = {num1 * num2}")

elif op == "/":
	total = num1 / num2
	print(f"{num1} / {num2} = {num1 / num2}")

elif op == "**":
	total = num1 ** num2
	print(f"{num1} ** {num2} = {num1 ** num2}")

elif op == "//":
	total = num1 // num2
	print(f"{num1} // {num2} = {num1 // num2}")

elif op == "%":
	total = num1 % num2
	print(f"{num1} % {num2} = {num1 % num2}")
else:
	print("you print an invalid operator, please a correct later")
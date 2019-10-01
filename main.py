try:
	namber1 = int(input("Число один: "))
	namber2 = int(input("Число два: "))
except ValueError:
	print("Ошибка!")

print("1. +")   # +
print("2. /")	# -
print("3. *")	# *
print("4. /")	# /
print("5. %")	# %

plus = "1"
minus = "2"
multiply = "3" 
divide = "4"
percentage = "5"

user = input("Выберите значение: ")

if user == plus:
	input = namber1 + namber2
	print(input)
elif user == minus:
	input = namber1 - namber2
	print(input)
elif user == multiply:
	input = namber1 * namber2
	print(input)
elif user == divide:
	input = namber1 / namber2
	print(input)
elif user == percentage:
	input = namber1 % namber2
	print(input)

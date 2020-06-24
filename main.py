import random
x = input("insert a number")
n = random.randint(1,100)
while true:
	if x == n:
		print("You guessed the number")
	if x < n:
		print("Try higher")
	if x > n:
		print("Try lower")

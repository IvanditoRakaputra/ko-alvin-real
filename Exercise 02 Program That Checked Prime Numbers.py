n =int(input(" Enter a number: "))

if n > 1:
	for i in range(2, n-1):
		if (n % i) == 0:
			print(n, ", that is not a prime number!!!")
		break
	else:
		print(n, ", that is a prime number!!!")

else:
	print(n, ", that is not a prime number!!!")
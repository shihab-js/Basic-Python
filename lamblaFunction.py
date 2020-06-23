num = int(input("Please enter a integer number: "))
result = lambda num : num % 2

if result(num) == 0:
    print("Congratulations! You Enter a prime number.")
else:
    print("Congratulations! You Enter a non-prime number.")
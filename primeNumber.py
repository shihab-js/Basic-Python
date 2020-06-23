
def isPrime(num):
    if num % 2 == 0:
        print("Congratulations! You enter a prime number.")
    else:
        print("Congratulations! You enter a non-prime number.")

num = int(input("Please inter a integer number: "))

isPrime(num)

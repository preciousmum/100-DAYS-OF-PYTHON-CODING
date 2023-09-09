# The goal of this program is to write a code that checks if a number is a prime number

def prime_checker(number):
# a prime number is a number that is divisibe by itself and one without any remainder
# for a number to be a prime number, it must be divided by other numbers to see if there would be a remainder or not

    is_prime = True #code to check the the prime number is true
    for i in range(2, number -1):
        if number % i == 0:
            is_prime = False
    if is_prime:
            print("It's a prime number.")
    else:
            print("It's not a prime number.")



n = int(input("check this number: "))
prime_checker(number=n)







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






# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)

# The for loop is used to print or get out all the possible ranges of numbers between the choices
# The modulo function was used to checke the numbers if its remainder is zero then it is not a prime as i contains
# values of greater than 2 
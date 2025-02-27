# 1.checking number polindroem 
num = int(input("enter the number"))
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")
  
  
# 2.Implement a menu-driven program where the user can chose to
#1. Find the square of a number.
#2. Find the cube of a number.
#until enter exit
#3. Exit.



def find_square(num):
    return num ** 2

def find_cube(num):
    return num ** 3

def menu():
    while True:
        
        print("1. Find the square of a number.")
        print("2. Find the cube of a number.")
        print("3. Exit.")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            num = float(input("Enter a number to find its square: "))
            print(f"The square of {num} is {find_square(num)}.")
        elif choice == '2':
            num = float(input("Enter a number to find its cube: "))
            print(f"The cube of {num} is {find_cube(num)}.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
menu()
#============================================================================================

# 3.perfect number
# the sum of all factors of a number is equal to that number then that number is perfect number
#ex 6----- factord of six are 1,2,3,6
#                             1+2+3=6 so 6 six is perfect number


def is_perfect_number(num):
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == num:
        return True
    else:
        return False

num = int(input("Enter a number to check if it's a perfect number: "))
if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
    
    
# 4.Implement a basic login system where the user has three attempts to enter the correct password using a loop..
    
correct_password = "password123"
attempts = 3
for i in range(attempts):
    entered_password = input("Enter your password: ")
    if entered_password == correct_password:
        print("Login successful!")
        break  
    else:
        print(f"Incorrect password. You have {attempts - i - 1} attempts left.")
else:
    print("Sorry, out of attempts log in later")

        

# 5.lcd 




# 6.gcd





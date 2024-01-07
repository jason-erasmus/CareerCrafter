# ---- Module imports
import re

"""
1. Welcome to x... please fill in your details to register
2. Name
3. Surname
4. mobile number
5. email r"^\S+@\S+\.S+$
6. salary expectations
7. notice period
8. RTW
9 create an interface with tk enter
"""

# User inputs

user_name = input("Please enter your name: ")
user_surname = input("Please enter your surname: ")
user_mobile = input("Enter mobile: ")
user_email = input("Enter email: ")
# user_salary = input("Enter your salary: ")
# user_notice = input("Enter your notice period: ")


# add except for input error


try:
    if user_name.isalpha():
        print(f"Thanks, your name is {user_name}")
    else:
        print(
            "Invalid input. Please enter a name without numbers or special characters."
        )
except ValueError:
    print("User name contains invalid characters")
except Exception as e:
    print(f"An error occurred: {e}")

# Verifying user_surname input
try:
    if user_surname.replace(" ", "").replace("-", "").isalpha():
        print(f"Thanks, your surname is {user_surname}")
    else:
        print(
            "Invalid input. Please enter a name without numbers or special characters."
        )

except Exception as e:
    print(f"An error occurred: {e}")

# Verifying user mobile number input

verify_phone_number = r"^\+?[0-9]\d*$"
cleaned_input = user_mobile.replace(" ", "")
number_verification = re.fullmatch(verify_phone_number, cleaned_input)
if number_verification is not None:
    print("Thank you")
else:
    print("Please enter a valid mobile number")

verify_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email_verification = re.match(verify_email, user_email)
if email_verification is not None:
    print("Thank you for entering your email address")
else:
    print("Please enter a valid email address")

print(f"Thank you for entering your details")

# ---- Module imports
import re
import tkinter

import customtkinter

# ---- GUI setup

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("800x500")

# Internal border
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

user_name = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
user_name.pack(pady=12, padx=10)

user_surname = customtkinter.CTkEntry(master=frame, placeholder_text="Surname")
user_surname.pack(pady=12, padx=10)

mobile_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Mobile Number ")
mobile_entry.pack(pady=12, padx=10)


# add except for input error
# --- Submit Button Function


def submit_button():
    user_name_func()
    surname_func()
    mobile_number_func()


# ---- verify user_name input
def user_name_func():
    try:
        entered_name = user_name.get()
        if entered_name.isalpha():
            print(f"Thanks, your name is {entered_name}")
        else:
            print(
                "Invalid input. Please enter a name without numbers or special characters."
            )
    except ValueError:
        print("User name contains invalid characters")
    except Exception as e:
        print(f"An error occurred: {e}")


# ---- Verifying user_surname input


def surname_func():
    surname = user_surname.get()
    try:
        if surname.replace(" ", "").replace("-", "").isalpha():
            print(f"Thanks, your surname is {surname}")
        else:
            print(
                "Invalid input. Please enter a name without numbers or special characters."
            )

    except Exception as e:
        print(f"An error occurred: {e}")


# # ---- Verifying user mobile number input
def mobile_number_func():
    user_mobile = mobile_entry.get()
    verify_phone_number = r"^\+?[0-9]\d*$"
    cleaned_input = user_mobile.replace(" ", "")
    number_verification = re.fullmatch(verify_phone_number, cleaned_input)
    if number_verification is not None:
        print(f"Thank you your mobile number is: {cleaned_input}")
    else:
        print("Please enter a valid mobile number")


# # ---- verify email input
# verify_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
# email_verification = re.match(verify_email, user_email)
# if email_verification is not None:
#     print("Thank you for entering your email address")
# else:
#     print("Please enter a valid email address")

# print(f"Thank you for entering your details")

submit = customtkinter.CTkButton(master=root, text="Submit", command=submit_button)
submit.pack(pady=12, padx=10)

root.mainloop()

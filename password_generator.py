import random

lowercase_letters_string = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
int_string = '0123456789'
special_char_string = """`~!@#$%^&*()-_=+|]}[{'";:?.>,<"""

potential_password_char_list = []
generated_password = ''

length_determined = False
while length_determined == False:
    try:
        number_of_characters = int(input("How many characters would you like in your password? (8-128):   "))
        if number_of_characters < 8 or number_of_characters > 128:
            print("You must select a length between 8 and 128 characters. Please select a valid length.")
            length_determined = False
        else:
            length_determined = True
    except ValueError:
        print("Please enter a valid integer character(must be between 8 and 128).")

while bool(potential_password_char_list) == False:
    print("\nPlease select at least 1 of the following 4 potential character sets:")
    lowercase_confirm = input("\nWould you like lowercase letter characters in your random password? (yes / no):   ")
    if 'yes' in lowercase_confirm.lower():
        potential_password_char_list.append(lowercase_letters_string)
        print(potential_password_char_list)
    uppercase_confirm = input("\nWould you like uppercase letter characters in your random password? (yes / no):   ")
    if 'yes' in uppercase_confirm.lower():
        potential_password_char_list.append(uppercase_letters_string)
        print(potential_password_char_list)
    int_confirm = input("\nWould you like integer characters in your random password? (yes / no):   ")
    if 'yes' in int_confirm.lower():
        potential_password_char_list.append(int_string)
        print(potential_password_char_list)
    special_char_confirm = input("\nWould you like special characters in your random password? (yes / no):   ")
    if 'yes' in special_char_confirm.lower():
        potential_password_char_list.append(special_char_string)
        print(potential_password_char_list)
    if bool(potential_password_char_list) == False:
        print("\nPlease select at least 1 valid character set.")


for x in range(0,  number_of_characters):
    selected_set = random.choice(potential_password_char_list)
    selected_character = random.choice(selected_set)
    generated_password += selected_character

print(f"""
Your new randomly generated password is: 

{generated_password}

Thanks for using Python Password Generator!""")

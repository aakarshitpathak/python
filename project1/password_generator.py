import random 
import string 

def generate_password(length):
    if length < 4:
        return "Password should be at least 4 characters long."
    
    # characters to choose from
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Ensure password includes at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length
    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4) 

    #shuffle the list to make it random
    random.shuffle(password)

    #join to make it a string
    return ''.join(password)

# Ask user for desired password length
try:
    user_length = int(input("Enter desired password length :"))
    print("Passowrd Generated:",generate_password(user_length))
except ValueError:
    print("Please enter a balid number.")


import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Prompt the user to specify the desired length of the password
length = int(input("Enter the desired length for the password: "))

# Generate the password
password = generate_password(length)

# Display the generated password
print(f"Generated password: {password}")


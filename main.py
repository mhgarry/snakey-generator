import secrets # import secrets module for generating random characters
import string # import string module for string operations

# variables for letters, digits, and special characters to be used in later generated passwords 
letters = string.ascii_letters # generates all lowercase and uppercase letters in the alphabet
digits = string.digits # generates all digits from 0-9
special_chars = string.punctuation # generates all special characters we are using in this program

available_chars = letters + digits + special_chars # defines all characters that are available to be used in the password

password = '' # intializes password variable to be used later

for i in range(12, 124):
    password += secrets.choice(available_chars) # adds a random character from the available characters to the password variable
    
print(password)
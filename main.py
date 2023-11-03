import secrets # import secrets module for generating random characters
import string # import string module for string operations
import tkinter as tk # import tkinter module to make GUI

# print(password)
def generate_password():
    letters = string.ascii_letters # generates all lowercase and uppercase letters in the alphabet
    digits = string.digits # generate all digits from 0-9
    special_chars = string.punctuation # generates all special characters we are using in this program
    available_chars = letters + digits + special_chars # defines all characters that are available to be used in the password
    
    password = '' # initializes password variable to be used later
    for i in range(12, 124):
        password += secrets.choice(available_chars) # adds a random character from the available characters to the password variable on each iteration of the loop
        
    password_label.config(text=password) # sets the text of the password_label to the generated password to represent it on the GUI
    
# create application window 
root = tk.Tk() # initializes the root window
root.title("Password Generator") # sets the title of the root window to password generator

# create a password display label 
password_label = tk.Label(root, font=('Helvetica', 18, 'bold')) # initializes the password_label and sets the font to Helvetica, size to 18, and bolds the text
password_label.pack(pady=10) # fixes the position of the password label to the root window

# create a button to generate the password 
generate_button = tk.Button(root, text="Generate Password", command=generate_password) # initializes a button to generate a password using the generate_password function
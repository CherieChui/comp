from builtins import input
import os

def create_pir():
    file_name = input("Enter the file name for the new PIR: ")

    if os.path.exists(file_name):
        print(file_name + " file already exists.")
    else:
        try:
            with open(file_name, 'w') as file:
                print("New PIR created: " + file_name)
            with open(file_name, 'r') as file:
                pir_text = file.read()
                if pir_text:
                    print("PIR content:")
                    print(pir_text)
                else:
                    print("Empty PIR file.")
        except IOError:
            print("Error: Unable to create or open the PIR file.")

create_pir()

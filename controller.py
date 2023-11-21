# Filename: controller.py

import os
import sys
from model import PIM
from view import Manage_PIR

def check_whether_file_exist(file_path):
    return os.path.isfile(file_path)

def print_all_files():
    print("All files:")
    # Assuming you want to print all files in the current directory
    for file_name in os.listdir(os.getcwd()):
        if file_name.endswith(".pim"):
            print(file_name)
    return True

def main():
    current_path = os.getcwd()

    print("")
    print("----------------------------------------------")
    print("Welcome to the Personal Information Management")
    print("----------------------------------------------")
    while True:
        print("-------Menu-------")
        print("1. Create a new PIR")
        print("2. Manage the PIR")
        print("3. Terminate the System")
        selection = input("Please choose one of the options above: ")
        if selection == '1':
            file = input("Please Enter a File Name (without '.pim'): ")
            filename = file + '.pim'
            file_path = current_path + '/' + filename
            while check_whether_file_exist(file_path) == True:
                print("The file already exists, please try again")
                file = input("Please Select one File Above (without '.pim'): ")
                filename = file + '.pim'
                file_path = current_path + '/' + filename
                
            pim = PIM(filename)
            if Manage_PIR(pim) == "back":
                continue

        elif selection == '2':
            while print_all_files():
                file = input("Please Select one File Above (without '.pim'): ")
                filename = file + '.pim'
                file_path = current_path + '/' + filename
                while check_whether_file_exist(file_path) != True:
                    print("The file does not exist, please try again")
                    file = input("Please Select one File Above (without '.pim'): ")
                    filename = file + '.pim'
                    file_path = current_path + '/' + filename
                    
                pim = PIM(filename)
                if Manage_PIR(pim) == "back":
                    break

        elif selection == '3':
            sys.exit()

        else:
            print("Invalid input, Please try again")

if __name__ == "__main__":
    main()

import os
current_path = os.getcwd()

def print_specific_PIR():
    file_name = input("Please chooce the PIR you want print(without '.txt'): ")
    file_path = current_path + '/' + file_name + '.txt'
    
    if os.path.exists(file_path):
        with open(file_path,'r') as file:
            file_content = file.read()
        print("")
        print("--------------------------------------------")
        print("Content displayed:")
        print(file_content)
    else:
        print("File does not exist or is not a text file, Please try again.")
        print("")
        print_specific_PIR()

def print_all_PIRs():
    for file_name in os.listdir(current_path):
        if file_name.endswith('.txt'):
            file_path = current_path + '/' + file_name
            with open(file_path,'r') as file:
                file_content = file.read()
            print("----------------------------------------")
            print("FILE NAME: ", file_name)
            print("CONTENT: ", file_content)
            


#print_specific_PIR()  display a specific PIR
#print_all_PIRs()      display all PIRs

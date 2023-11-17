import os

current_path = os.getcwd()

def display_file_name():
    List_of_files = os.listdir(current_path)
    print("The files exist in file displayed below:")
    print("----------------------------------------------")
    for file_name in List_of_files:
        if file_name.endswith('.txt'):
            print(file_name)
    print("----------------------------------------------")

def delete_file():
    file_name = input("Please enter the file you want to delete(without '.txt'): ")
    file_path = current_path + '/' + file_name + '.txt'

    if os.path.exists(file_path) and file_path.endswith(".txt"):
        # Delete the file
        os.remove(file_path)
        print("File deleted successfully.")
    else:
        print("File does not exist or is not a text file, Please try again.")
        print("")
        delete_file()
    
display_file_name()
delete_file()
    
    

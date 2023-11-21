# Filename: controller.py

from model import PIM
from view import Manage_PIR

def main():
    file_name = input("Enter the name of the file you want to open or create(without '.pim'): ") + '.pim'
    pim = PIM(file_name)
    Manage_PIR(pim)

if __name__ == "__main__":
    main()

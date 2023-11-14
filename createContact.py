class createContact:
    def __init__(self,name,addr,phone):
        self.name=name
        self.addr=addr
        self.phone=phone

    def __str__(self):
        return f"Name:{self.name}, Address:{self.addr}, Mobile Phone:{self.phone}"

    def getName(self):
        return self.name

    def getAddr(self):
        return self.addr

    def getPhone(self):
        return self.phone

def create(array):
    name=input("Name:")
    addr=input("Address:")
    phone=input("Phone:")

    contact=createContact(name,addr,phone)
    array.append(contact)
    print("Success:",contact)

array=[]
create(array)


    

from PIR import PIR 

class PIM():
    def __init__(self):
        self.PIRs={}

    def start(self):
        while True:
            self.menu()
            selection=input("Please enter a number:")
            num=int(selection)
            if num<=5 and num>=0:
                self.selectmenu(selection)
            else:
                print("Please enter correct number:")

    def menu(self):
        print("Menu")
        print("1. Create Contact")
        print("2. Modify Contact")
        print("3. Search Contact")
        print("4. Delete Contact")

    def selectmenu(self,num):
        select={"1":self.createContact,
                "2":self.modifyContact,
                "3":self.searchContact,
                "4":self.deleteContact}
        if selection=="2" or "3" or "4":
            typeinformation=input("Which information you want to type in to search(Name/Address/Mobile Phone):")
            if typeinformation=="Name" or "name":
                name=input("Please enter the name:")
                selectmenu[selection](name)
            elif typeinformation=="Address" or "address":
                addr=input("Please enter the address:")
                selectmenu[selection](addr)
            elif typeinformation=="Mobile Phone" or "mobile phone":
                name=input("Please enter the phone number:")
                selectmenu[selection](phone)
            else:
                selectmenu[selection]()
                

    def createContact(self):
        name=input("Name:")
        addr=input("Address:")
        phone=input("Mobile Phone:")
        contact=PIR(name,addr,phone)
        self.PIRs[phone]=contact

    def modifyContact(self,name,addr,phone):
        print("Searching:")
        people=self.searchContact(name,addr,phone)
        if people:
            contact=self.PIR[people]
            ans=input("Name need to modify (If no need, please input None):")
            contact.name=self.modifyJudge(ans,contact.name)
            ans=input("Address need to modify (If no need, please input None):")
            contact.addr=self.modifyJudge(ans,contact.addr)
            ans=input("Mobile Phone need to modify (If no need, please input None):")
            contact.phone=self.modifyJudge(ans,contact.phone)
            print("Finish")

    def modifyJudge(self,ans,value):
        if ans=="None" or "none":
            return value
        else:
            return ans

    def searchContact(self,name,addr,phone):
        for people in self.PIRs:
            if people == name or addr or phone:
                self.printppl(people)
                return people
            else:
                print("Do not have this contact.")
                return None

    def printppl(self, phone):
        print(str(self.PIRs[phone]))

    def deleteContact(self,phone):
        people=self.searchContact(name,addr,phone)
        if people:
            self.PIRs.pop(people)
            print("Delete Successful")



        

class PIR(object):
    def __init__(self,name,addr,phone):
        self.name=name
        self.addr=addr
        self.phone=phone

    def __str__(self):
        return self.name+self.addr+self.phone
        

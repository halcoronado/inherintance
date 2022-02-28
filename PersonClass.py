class Person:
    def __init__(self, pname, address, phonenum):
        self.__pname = pname
        self.__address = address 
        self.__phonenum = phonenum

    def print_person(self):
        print(self.__pname)
        print(self.__address)
        print(self.__phonenum)

class Customer(Person):
    def __init__ ( self, custnum, maillist,  pname, address, phonenum):
        Person.__init__(self, pname, address, phonenum)
        self.__custnum = custnum
        self.__maillist = maillist
    
    def print_person(self):
        Person.print_person(self)
        print(self.__custnum)
        print(self.__maillist)
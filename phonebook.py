class contact:
    def __init__(self):
        self.f_name=input('Enter the first name of the contact : ')
        self.l_name=input('Enter the last name of the contact : ')
        self.phone_no=input('Enter the phone number of the contact : ')
    def put_data(self):
            f=open("phonebook.txt","a")
            f.write(self.f_name+"    "+self.l_name+"    "+self.phone_no+"\n")
            f.close()
            print("Data entered successfully! ")
    def get_data(self):
        f=open("phonebook.txt","r")
        print("The contents of the file are : \n")
        print(f.read())
        f.close()

c1=contact()

c1.get_data()
'''c1.put_data()
c2=contact()
c2.put_data()
c2.get_data()'''

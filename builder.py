"""
Name: Filmon Araya
Week_5_
"""
class PersonalDataForm():
    def __init__(self,first_name,last_name,email,phone,address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        
    def get_fullName(self):
        return self.first_name+' '+self.last_name
    
    def __str__( self ):
        return 'user info: firstname = '+self.first_name, 'lastname = '+self.last_name, 'address = '+self.address, 'email = '+self.email, 'phone = '+self.phone, 'address= '+self.address       

class UserDetails():
    def __init__(self,title,gender,notes):
        self.title = title
        self.gender = gender
        self.notes = notes
    
    def __str__(self):
        return 'user detail: '+ self.title,self.gender,self.notes
    
class FieldCollectionForm(models.Model):
    """This class will develop fully using django models
        The model that needs to thats needs to ask questions.
         name = models.CharField(max_length=256)
         questions = models.ManyToManyField(Question)

        """
    pass
    
def main():
    p = PersonalDataForm('Filmon','Araya','fili@example.com','123-456-7891', '123 str,city,state')
    fullname=p.get_fullName()
    u=UserDetails('Mr', 'Male', 'This is test code')
    print(fullname)
    print(p.__str__())
    print(u.__str__())

    #s = str(p)
    #print(s)
    
main()


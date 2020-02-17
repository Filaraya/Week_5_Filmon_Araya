"""
Name: Filmon Araya
week 5
design pattern: facade
"""
#In my field data collector app, I am going use facade for a database connection
class Login:
    error = None
    def __init__(self, uid, passw):
        self.uid = "admin"
        self.passw = "admin"
        Login.error = "Enter a valid user id and password"

    def authenticate(self):
        if (self.uid == logid and self.passw == logpass):
            print ("Login successful")
        else:
            print (Login.error)
log = Login("", "")
logid = input("Enter your user ID: ")
logpass = input("Enter your password: ")


log.authenticate()
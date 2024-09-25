import smtplib

class User:
    __name = "Jane"
    __age = 30
    __email = "jane@test.com"
    __location = "Lagos"

    def __init__(self, name, age, email, location):
        self.__name = name
        self.__age = age
        self.__email = email
        self.__location = location


    @classmethod
    def get_userdata(cls):
        return {
            'name': cls.__name,
            'age': cls.__age,
            'email': cls.__email,
            'location': cls.__location
        }
    

    @classmethod
    def set_userdata(cls, new_name, new_age, new_email, new_location):
        cls.__name = new_name
        cls.__age = new_age
        cls.__email = new_email
        cls.__location = new_location
    

    def send_email(self):
        if self.__email:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(sender_email, sender_password)
            message = f"A new user created, {self.__name}"
            s.sendmail(sender_email, self.__email, message)
            s.quit()


    def __str__(self):
        return f"{self.__name} with {self.__email} is {self.__age} and lives in {self.__location}"


#instaciating the class user
user1 = User("Lola", 10, "teboola@yahoo.com", "Ibadan")
user1.send_email()
print(user1)
# print(User.get_userdata())
#overriding the class atrribute
# User.set_userdata("John", 25, "john@test.com", "London")
# print(User.get_userdata())



class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        return f'Person information: \nName: {self.name} {self.last_name}\nPhone number: {self.phone_number}\n'\
               f'Address: {self.address}\nEmail: {self.email}\n'\
               f'Date of birth: {self.birthday}\nAge: {self.age}\nGender: {self.sex}'


if __name__ == "main":
    profile = Profile('Vinson', 'Sterling', '489-52-75', '897 Vinewood Hills, Los Santos, SA, 95249',
                      'vinssterling@gmail.com', '28.04.1975', '46', 'Male')
    print(profile)

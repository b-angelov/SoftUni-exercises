from re import match

class Profile:

    def __init__(self,username: str, password: str):
        self.set_username(username)
        self.set_password(password)


    def set_username(self,username:str):
        if not match(r"^.{5,15}$",username):
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = username

    def set_password(self,password:str):
        if not match(r"^(?=.*[A-Z])(?=.*\d).{8,}",password):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = password

    def get_password(self):
        return self.__password

    def get_username(self):
        return self.__username

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'

# profile_with_invalid_password = Profile('My_username', 'My-password')

# profile_with_invalid_username = Profile('Too_long_username', 'Any')

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)

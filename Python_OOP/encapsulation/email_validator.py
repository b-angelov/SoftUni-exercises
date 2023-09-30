
class EmailValidator:

    def __init__(self,*args):
        self.__min_length,self.__mails,self.__domains = args

    def __set_min_length(self,value: int):
        print("gdgg")
        self.__min_length = value

    def __set_valid_mails(self,valid_mails: list):
        self.__mails = valid_mails

    def __set_valid_domains(self,domains: list):
        self.__domains = domains

    min_length = property(fset=__set_min_length)
    mails = property(fset=__set_valid_mails)
    domains = property(fset=__set_valid_domains)

    def __is_name_valid(self,name):
        return len(name) >= self.__min_length

    def __is_mail_valid(self,mail):
        return mail in self.__mails

    def __is_domain_valid(self,domain):
        return domain in self.__domains

    def validate(self,email):
        first,second = email.split(".")
        name,mail,domain = (*first.split("@"),second)
        return all((self.__is_name_valid(name),self.__is_mail_valid(mail),self.__is_domain_valid(domain)))

mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))



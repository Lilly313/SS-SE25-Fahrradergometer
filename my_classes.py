from my_functions_Ida import estimate_max_hr
from datetime import datetime

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Subject(Person):
    def __init__(self, first_name, last_name, sex, dateofbirth):
        super().__init__(first_name, last_name)
        if not isinstance(dateofbirth, datetime):
            raise ValueError("dateofbirth must be a datetime object")
        self.sex = sex
        self.__dateofbirth = dateofbirth
    
    def calculate_max_hr(self):
        return estimate_max_hr(self.get_age(), self.sex)
        
    def get_age(self):
        today = datetime.today()
        age = today.year - self.__dateofbirth.year - ((today.month, today.day) < (self.__dateofbirth.month, self.__dateofbirth.day))
        return age

class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# Beispiel für die Verwendung
subject = Subject("Ida", "Dürr-Pucher", "female", datetime.strptime("01/04/2004", "%d/%m/%Y"))
print(subject.get_age())
print(subject.calculate_max_hr())
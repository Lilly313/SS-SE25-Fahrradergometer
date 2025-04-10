from my_functions_Ida import estimate_max_hr
from datetime import datetime

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Subject(Person):
    def __init__(self, first_name, last_name, sex, dateofbirth):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.__dateofbirth = datetime.strptime(dateofbirth, "%d/%m/%Y")
    
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
    
class Experiment():
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def __str__(self):
        return f"{self.experiment_name} on {self.date} supervised by {self.supervisor} with subject {self.subject.first_name} {self.subject.last_name}"
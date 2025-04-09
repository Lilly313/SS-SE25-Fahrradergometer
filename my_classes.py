from my_functions_Lilly import estimate_max_hr
from datetime import datetime

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Subject(Person):
    def __init__(self, first_name, last_name, dateofbirth, sex):
        super().__init__(first_name, last_name)   
        self.__dateofbirth = dateofbirth
        self.sex = sex
    
    def get_age(self):  #orientiert an skript
        age =  datetime.today().year- self.__dateofbirth.year
        return age
    
    def estimate_max_hr(self):
        return estimate_max_hr(self.get_age(), self.sex)
    
class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)


class Experiment():
    def __init__(self, experiment_name, experiment_date):
        self.experiment_name = experiment_name
        self.experiment_date = experiment_date

    def add_subject(self, subject):
        self.subject = subject

    def add_supervisor(self, supervisor):
        self.supervisor = supervisor

    def __str__(self):
        return f"Experiment Name: {self.experiment_name}\nDate: {self.experiment_date}\nSubject: {self.subject.first_name} {self.subject.last_name}\nSupervisor: {self.supervisor.first_name} {self.supervisor.last_name}"
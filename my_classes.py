from my_functions_Lilly import estimate_max_hr

class Subject():
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def estimate_max_hr(self):
        return estimate_max_hr(self.age, self.sex)
    
class Supervisor():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Experiment():
    def __init__(self, experiment_name, date):
        self.experiment_name = experiment_name
        self.date = date

    def add_subject(self, subject):
        self.subject = subject

    def add_supervisor(self, supervisor):
        self.supervisor = supervisor

    def __str__(self):
        return f"Experiment Name: {self.experiment_name}\nDate: {self.date}\nSubject: {self.subject.first_name} {self.subject.last_name}\nSupervisor: {self.supervisor.first_name} {self.supervisor.last_name}"
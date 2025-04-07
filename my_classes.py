from my_functions_Ida import estimate_max_hr

class Subject():
    def __init__(self, subject : dict):
        self.subject = subject    
        self.max_hr = estimate_max_hr(subject["age"], subject["sex"])
        print(self.max_hr)
class Supervisor():
    def __init__(self, supervisor : dict):
        self.supervisor = supervisor
    pass

class Experiment():
    def __init__(self, experiment : dict):
        self.experiment = experiment
    pass

Subject({"id" : 1, "FirstName" : "Ida", "LastName" : "Dürr-Pucher", "sex" : "female", "age" : 21,})
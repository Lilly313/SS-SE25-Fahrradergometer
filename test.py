from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":

    subject = Subject({"id" : 1, "FirstName" : "Ida", "LastName" : "Dürr-Pucher", "sex" : "female", "age" : 21})
    supervisor = Supervisor({"id" : 1, "FirstName" : "Ida", "LastName" : "Dürr-Pucher", "sex" : "female", "age" : 21})
    experiment = Experiment({"experiment_name" : "Experiment 1", "date" : "2023-10-01", "supervisor" : supervisor, "subject" : subject})
    
    print(subject.subject, supervisor.supervisor, experiment.experiment)
    
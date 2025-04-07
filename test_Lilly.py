from my_classes import Subject, Supervisor, Experiment
if __name__ == "__main__":

    # Erstellen eines Leistungstests
    supervisor = Supervisor("Julian", "Huber")
    subject = Subject("Lilly", "Feifel", "female", 20)
    subject.estimate_max_hr()

    experiment = Experiment("assignment61_max_heartrate", "2025-04-04")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)


    print(experiment)
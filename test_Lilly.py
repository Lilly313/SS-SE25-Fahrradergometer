from my_classes import Subject, Supervisor, Experiment
from datetime import datetime

if __name__ == "__main__":

    # Erstellen eines Leistungstests
    supervisor = Supervisor("Julian", "Huber")

    dateofbirth = datetime.strptime("31.03.2005", "%d.%m.%Y")  #orientiert an skript
    subject = Subject("Lilly", "Feifel", dateofbirth, "female")

    print("Geschätzte maximale Herzfrequenz:", subject.estimate_max_hr(), "bpm")

    experiment_date = datetime.strptime("09.04.2025", "%d.%m.%Y")
    experiment = Experiment("assignment62_max_heartrate", "2025-04-09")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)


    print(experiment)
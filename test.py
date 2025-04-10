from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":

    subject = Subject("Ida", "Dürr-Pucher", "female", "01/04/2004")
    supervisor = Supervisor("Julian", "Huber")
    experiment = Experiment("Experiment 1", "10/04/2025", supervisor, subject)
    
    print(subject, supervisor, experiment)
    
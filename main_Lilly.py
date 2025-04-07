from my_functions_Lilly import build_person, build_experiment

if __name__ == "__main__":
    first_name = "Lilly"
    last_name = "Feifel"
    sex = "female"
    age = 19
    age_years = age
    experiment_name = "assignment3_max_heartrate"
    date = "23.03.2025"
    supervisor = "Dr. Julian Huber"
    subject = "Sakai Assignment 3"

    teilnehmer = build_person(first_name, last_name, sex, age)
    experiment = build_experiment(experiment_name, date, supervisor, subject)

    print(teilnehmer)   
    print(experiment)

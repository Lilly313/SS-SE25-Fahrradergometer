def estimate_max_hr(age_years: int, sex: str) -> int:
    """
    Berechnet die maximale Herzfrequenz basierend auf Alter und Geschlecht.
    Siehe: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/
    """
    sex = sex.lower()  # Falls das Geschlecht in Großbuchstaben übergeben wird

    if sex == "male":
        max_hr_bpm = 223 - 0.9 * age_years
    elif sex == "female":
        max_hr_bpm = 226 - 1.0 * age_years
    else:
        raise ValueError("Ungültiges Geschlecht. Bitte 'male' oder 'female' angeben.")

    return int(max_hr_bpm)

def build_person(first_name, last_name, sex, age) -> dict:
    """Returns a dictionary of information about a supervisor or subject."""
    person_dict = { "first_name" : first_name,
             "last_name" : last_name,
             "age" : age,
             "estimate_max_hr" : estimate_max_hr(age,sex)}
    return person_dict

def build_experiment(experiment_name, date, supervisor, subject) -> dict:
    """Returns a dictionary of information about an experiment."""
    experiment_dict = {"experiment_name" : experiment_name,
            "date" : date,
            "supervisor" :   supervisor,
            "subject" :   subject
            }
    return experiment_dict

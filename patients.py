PATIENT_1 = {"NAME": "SAM", "WEIGHT": 350, "SYST": 135, "DIAS": 85}
PATIENT_2 = {"NAME": "MARCOS", "WEIGHT": 150, "SYST": 125, "DIAS": 78}
PATIENT_3 = {"NAME": "DAVID", "WEIGHT": 250, "SYST": 128, "DIAS": 80}
PATIENT_4 = {"NAME": "LUIGI", "WEIGHT": 120, "SYST": 110, "DIAS": 75, "DREAMS": 0, "GROWTHS": 1, "MEMORY": 0}
PATIENT_5 = {"NAME": "LUIS", "WEIGHT": 180, "SYST": 125, "DIAS": 80, "DREAMS": 1, "GROWTHS": 0, "MEMORY": 1}
PATIENT_LIST = [PATIENT_1, PATIENT_2, PATIENT_3, PATIENT_4, PATIENT_5]


def patient_list(selection):
    return PATIENT_LIST[selection - 1]


def get_patient_list_length():
    return len(PATIENT_LIST)


def give_module_name():
    return "patients"

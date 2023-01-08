# CONSTANTS
HBP_SYSTOLIC = 130
HBP_DIASTOLIC = 80

TRUE_MSSG = "The Patient Is At Risk For Diabetes"
FALSE_MSSG = "The Patient Is Not At Rist For Diabetes"


def calculate(systolic, diastolic):
    if systolic > HBP_SYSTOLIC:
        return TRUE_MSSG
    elif systolic <= HBP_SYSTOLIC:
        if diastolic > HBP_DIASTOLIC:
            return TRUE_MSSG
        elif diastolic <= HBP_DIASTOLIC:
            return FALSE_MSSG


def give_module_name():
    return "diabetes"

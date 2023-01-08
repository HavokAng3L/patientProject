TRUE_MSG = "This Patient Is At Risk For ROOT DISEASE"
FALSE_MSG = 'This Patient Is Not At Rist For ROOT DISEASE'


def calculate(dreams, sprouts, memory):
    count = 0
    if dreams is True:
        count += 1

    print(count)

    if count > 1:
        return TRUE_MSG
    else:
        return FALSE_MSG


def give_module_name():
    return "root disease"

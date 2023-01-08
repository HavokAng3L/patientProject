# This Program Returns A Patients Chances Of
# Any Disease
from diseases import diabetes, root_disease
import patients
import os
DIR_PATH = "diseases"
CURRENT_MODULES = [diabetes.give_module_name(), root_disease.give_module_name()]
# NOTE: MUST BE A BETTER WAY TO LIST THE MODULES AVAILABLE


def main():
    counter = 0
    user_main_choice = 'y'

    while user_main_choice == 'y':
        counter += 1

        draw_menu(counter)

        selection = select_a_patient()

        patientObj = patients.patient_list(selection)

        display_info = select_a_module(counter)

        if display_info in CURRENT_MODULES[0]:
            print(diabetes.calculate(patientObj.get("SYST"), patientObj.get("DIAS")))
        elif display_info in CURRENT_MODULES[1]:
            print(root_disease.calculate(patientObj.get("DREAMS"), patientObj.get("GROWTHS"), patientObj.get("MEMORY")))

        user_main_choice = str(input("Would You Like To Check Another Patient? (y or n): "))


def draw_menu(counter):  # Draws the menu for the program
    if counter < 4:
        print(f"Hello, There are {patients.get_patient_list_length() - 2} patients in today.")
        for index in range(patients.get_patient_list_length() - 2):
            print(patients.patient_list(index + 1).get("NAME"))
    else:
        print(f"HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO, THERE AAAAAAAAAAAAAAAAAAAAAAAAARE {patients.get_patient_list_length()}")
        print("PATIENTS IN TOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOODAYYYY")
        for index in range(patients.get_patient_list_length()):
            print(patients.patient_list(index).get("NAME"))


def count_modules():
    count = 0
    for path in os.listdir(DIR_PATH):
        if os.path.isfile(os.path.join(DIR_PATH, path)):
            count += 1
    return count - 1


def select_a_patient():

    print(f"Make A Patient Selection "
          f"({patients.get_patient_list_length() - (patients.get_patient_list_length() - 1)}"
          f" to {patients.get_patient_list_length()})")

    userInput = int(input())
    print(f"{patients.patient_list(userInput).get('NAME')}")

    if userInput > 3:
        for i in range(10):
            if i < 5:
                input()
            else:
                input("IT IS NOT REAL.")
                input("ANSWER THE DOOR.")

    return userInput


def select_a_module(counter):
    if counter < 4:
        print(f"Select Which Disease {count_modules() - (count_modules() - 1)} to {count_modules() - 1}")
    else:
        print(f"Select Which Disease ({count_modules() - (count_modules() - 1)} to {count_modules()})")

    user_choice = int(input())
    if user_choice in range(len(CURRENT_MODULES)+1):
        print(CURRENT_MODULES[user_choice - 1].upper())

    else:
        print("Module Not Found.")

    return CURRENT_MODULES[user_choice - 1]


main()

# HSC4933 Lab 2: Functions, User Input, and Readable, Usable Code #
# Ankita Nair #

# Heart rate samples/data of the patients.
heart_rate_samples = {
"J. Alvarez": [72, 75, 78],
"M. Chen": [80, 82],
"R. Okafor": [65, 68, 70, 66],
"S. Patel": [90, 95, 92, 88, 91],
"T. Nguyen": [77, 79],
"L. Kowalski": [68, 70, 69],
"D. Osei": [98, 101, 95, 99],
"A. Whitfield": [74, 76, 75, 73],
}

# The following will write out the patient heart rate data.
def patient_stats(patient_name, *args):
    patient_data = heart_rate_samples[patient_name]

    # This loop will show the given patient data in the terminal when the user asks for whichever specific information they would like to see. That would be either the average, maximum, or minimum heart rates (of chosen pateint).
    for stat in args:
        if stat == "All of the heart rate information":
            print("Heart rate samples:")
            print(patient_data)

        elif stat == "Average heart rate":
            average = sum(patient_data) /len(patient_data)
            print("Average heart rate:")
            print(average)

        elif stat == "Minimum heart rate":
            print("Minimum heart rate:")
            print(min(patient_data))

        elif stat == "Maximum heart rate":
            print("Maximum heart rate:")
            print(max(patient_data))

        else:
            print("Wrong input")

# This line of code will print out all of the patient names that was given with the data (in the terminal).
print("List of patients:")
for patient in heart_rate_samples:
    print(patient)

# The following line will allow the user to input/choose which patient's data they would like to see.
patient_name = input("Enter patient name: ")

# The following are the options of which form of heart rate stats the user would like to see.
print(" ")
print("Patients' heart rate information:")
print("Average heart rate")
print("Minimum heart rate")
print("Maximum heart rate")

# This line of code will be asking for the stat.
statistic = input("Enter the patient statistic you would like to see: ")

# This following line will display when the patient stats input is wrong/invalid and it will ask again for patient stats to be retrieved (until valid input is given by the user).
while statistic != "All of the heart rate information" and statistic != "Average heart rate" and statistic != "Minimum heart rate" and statistic != "Maximum heart rate":
    print("Wrong input")
    statistic = input("Enter the patient statistic you would like to see: ")

# This will display the information after running it whcih includes both the patients names and their heart rate date (average, minimum, maximum).
patient_stats(patient_name, statistic)

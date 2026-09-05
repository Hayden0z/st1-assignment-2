print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name = input("insert 1st patient name")
practitioner1_name = input("insert 1st practitioner name")
appointment1_time = input("Date and Time")
#Format string 
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")
# Second Appointment
patient2_name = input("insert 2nd patient name")
practitioner2_name = input("insert 2nd practitioner name")
appointment2_time = input("Date and Time")
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")

#limations 
#1 You can onlyl input one patient each time the code runs. I would have added a While True input loop, based on if a user wanted to add a nother patient or not but kept it simple as per assignment request.
#2none of the appioment schedudles are saved to a file or a database so are just present one run of the code.
#3 all future appioments needed to be fully added manually in the code and set all the variables, or I implement the While loop.
#4 No error handling to check variable type e.g date/time format if a user enters valid data. or if there is a valid practitioner or a spelling errot.
#5 No if else statements 
#6 No way of being able to modify or delting already existing appoiment schedules


print("Welcome to SmartCare: The Clinical Appointment Booking System!")
appointments = []
def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    appointment = {
    "patient": patient_name,
    "practitioner": practitioner_name,
    "time": appointment_time
     }
    appointments.append(appointment)

# this function check if patient name has a value and IF not raises an error message. If it is not empty it will add patient_name, practitioner_name, appointment_time variables and puts them in a dictionary and then adds that dictionary to the appointments list.

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner:{appointment['practitioner']} | Time: {appointment['time']}")

# this function does an IF statemetns to see if there is any value in the apoointments list. If empty is says no appointments, otherwise it will print all the dictionary values in the list.

book_appointment(patient1_name, practitioner1_name, appointment1_time)
book_appointment(patient2_name, practitioner2_name, appointment2_time)
display_appointments()

#limations
#not much data structure the only structure is the appoiment list
#no user intreaction it relies on the input from the first section so there errors in data type, including No checking of invalid or wrong time
# No formating 
# it is not retrieving from a secure database so you cant search or edit or update.
# the practitioner isn't checked for being valid so you cant sort by practitioner for example. Lots of features are missing.


#AI version
#appointments = []

#def book_appointment(patient, practitioner, time):
   # Basic checks to ensure all three fields are provided
#    if not patient:
#    print("Error: Patient name is required.")
#        return
#    if not practitioner:
#        print("Error: Practitioner name is required.")
#        return
#    if not time:
#        print("Error: Appointment time is required.")
#        return
#
#    appointment = {
#        "patient": patient,
#        "practitioner": practitioner,
#        "time": time
#    }
#
#    appointments.append(appointment)
#    print("Appointment stored.")
#
#def show_appointments():
#    if not appointments:
#        print("No appointments recorded.")
#
# 
#         return

#    for appt in appointments:
#        print(f"Patient: {appt['patient']} | Practitioner: {appt['practitioner']} | Time: {appt['time']}")

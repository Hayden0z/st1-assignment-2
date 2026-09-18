Candidate concepts

Candidate                           Class?                                                   Reason
Patient                            Is a class                                Patient as multiple attributes being name,age,gender ect 

Practioner                         Is a class                               Same as the patient with them having name,gender, 

Appointment                        Is a class                               Will have attributes like time,type,room,

Name                              Not a class                               Is an attribute for a patient or practitioner 

Clinic                            is A class            Clinic is a physical location which will have attributes like location and opening hours 

Database                          Not a class                   A database is something that holds all the information is just a implantation 

Cancellation                     Not a class                 Is just a check for if the appointment is available is just a state to see if the appointment is happening 

Status                           Not a class                      Status is an attribute for appointment as it i checks an appointment status 







CRC Cards 

Patient 

Responsibilities                                                                                    
Allow Staff  to change and update patient information when need  
Provide staff searchable patient information when finding patient in database  
Give patient details to staff to store(name,DOb,etc)


 Collaborators 
Practitioner- checks on the patient and views everything to prepare to meet with the patient  
Appointment - links to to patients appointment history
Receptionist-Search, updates and creates patient records  


Practitioner 

Responsibilities 
Store practitioner details(name,age,DOB,etc)
Allowed to look at patient records when preparing for an appointment 
Provide practitioners availability for scheduling 

Collaborators 
Appointment - practitioners are assigned to a appointment 
Patient- practitioners search and look though patient information to prepare for the appointment 
Receptionist-can update practitioner’s appointments to another time and update their record 


Appointment 

Responsibilities 
Prevent duplicate bookings 
Store appointment details(date,time,etc) 
Allow Receptionist to update appointment details 
Allow Receptionist to cancel appointment 


Collaborators 
Patients -links to to patients appointment history  
Appointment - practitioners are assigned to an appointment 
Receptionist-can create,update,cancel and manage booked and upcoming appointments 



Relationship Reasoning

Patient to Appointment: which relationship and why?
A one to many relationship 
Because a patient can have multiple appointments as time goes on.While an appointment is linked to one patient and every appointment is different so a single patient will have multiple appointments while there is just one unique appointment that will not have another patient just the one.     


Practitioner to Appointment: what multiplicity?
Practitioner 1 0..* Appointments;
each Appointment has exactly one Practitioner


Should Appointment inherit from the Patient?
Patient Appointment is best treated as an association, not composition They’re simply linked. Patients can exist without any appointments, and appointments are created, updated, or cancelled independently



Does Clinic need to own every object?
No has the clinic is just the organization it doesn't really own patient or practitioner or recipient because there can move to a different organization, and deleting the clinic information with own every object.will delete everything on practitioner,appointments,patients and recipients so no clinic does not need to own every object   




AI Model critique
Critique AI proposals: 

PatientManager, 
PatientManager is unnecessary and should not be included.  
It would be redundant, because every responsibility it would perform is already owned by the Patient class or by existing collaborators such as Receptionist and Appointment.


PractitionerManager,
PractitionerManager is unnecessary because it duplicates the responsibilities already assigned to the Practitioner class. It would conflict with the Practitioner CRC card 


AppointmentManager, 
is unnecessary and causes the same problems as PatientManager and PractitionerManager.  
It would duplicate the responsibilities already defined in the Appointment CRC card and create confusion about which class actually handles booking, updating, cancelling, and displaying appointments.  


ClinicController,
It isn’t a real thing the clinic uses, it has no responsibilities in the requirements, and anything it would do is already handled by a Patient, Practitioner, Receptionist, or Appointment.


NotificationManager, 
Notifications aren’t part of the clinic’s core workflow, the smart care requirements don’t mention sending reminders or alerts as confirmed features.So a NotificationManager would be an extra class with no real responsibilities


ScheduleEngine.
ScheduleEngine doesn’t really make sense for SmartCare.Appointments and practitioner availability already handle all the scheduling on their own, so adding a Schedule would just repeat the same work and make things more complicated than they need to be.

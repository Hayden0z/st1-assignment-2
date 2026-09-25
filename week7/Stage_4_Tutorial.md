Activity 1 - Encapsulation Review

Class 
Patient 

Protected state / invariant 
PatientID,age,DOB,History,contact_details 

Public operations
getage(),viewmedicalrecord(),allowed_appointments(),update_contact_details() 

Class 
Practitioner

Protected state / invariant 
PractionerID,name,speciality,availability_slots,status  

Public operations
isAvailable(),getspeciality(),assign appointments(),updateAvailability(),supsandRegstraion() 

Class 
Appointment

Protected state / invariant 
AppointmentID,Time,location,type,status,Patient,Practitioner  

Public operations
CancelAppointment(),completedAppioment(),getSummary(),rescheduleAppioment,validateAppioment() 



Activity 2 - Composition or Inheritance?
Appointment and Patient -> □ Composition/association Reason: every appointment has a patient,however the patient exists independently from Appointment,appioment just references a appointment that is why it is Composition/association 


Appointment and Practitioner -> □ Composition/association Reason: same thing as patient and Appointment.practioners can have many Appointment’s.while an appointment can have only one practitioner.    


Doctor and Practitioner (hypothetical) -> □ Inheritance Reason: Doctors are a type of practitioners.SO the two classes would share alot of the same attributes and behaviour.However doctor will have its own attributes and behaviours as a doctor is a more advanced Practitioner    
 


Clinic and Appointment -> □ Composition/association Reason: clinics contain appointments,however appointment exist independently being in the system even when a clinic closes  


Activity 3 - Responsibility Allocation

Who decides whether SCHEDULED can become CANCELLED?
The appointment class   

Who validates a patient name?
The patient class itself as it is responsible for checking that it’s own data is valid for example checking that name isn’t empty  

Should Appointment execute SQL? Why?
No appointment should not run SQL.SQL belongs in repository access layer.to keep everything clean and separated   


Should the UI decide whether a status transition is legal?
No The UI only displays options 



Activity 4 - AI Code Critique
AI generates an Appointment class with public status mutation, SQL inside cancel(), a NotificationManager dependency and inheritance from PatientRecord. Identify at least five design problems and corrections.

Design problems 
1.inheriting from PatientRecord
The problem is that the inheritance of Appointment to patient record is incorrect as appointment is not a type of Patient record 

 The corrections would be using Composition/association instead so that appointment has a Patient record but does not inherit anything       


2.SQL inside cancel() causes business and database logic to mix which makes the appointment class really hard to test 

The correction is to put the SQL into a repository instead      

3.The Appointment class is doing too much: status management, SQL, notifications, and inherited PatientRecord behaviour. This violates the Single Responsibility Principle and makes the class fragile.

Correction to split everything up example from earlier SQL being in a repository       


4.To much dependency on NotificationManger as appointment becomes to coupled and you are unable to reuse Appointment without also using NotificationManger 

The correction would to use an event system so when an event like CancelAppointment happens a different component handles the notifications            




5,Status is public, so anyone can change it directly. This breaks encapsulation and allows invalid state changes.

  The corrections would be to make Status private 




Exit question
Why can code be object-oriented syntactically but still have poor object-oriented design?
Because just using classes and objects doesn’t guarantee good object‑oriented design. Code can look object‑oriented but still be deeply flawed. It might use inheritance incorrectly, fail to use encapsulation, mix different types of logic together, or put responsibilities in the wrong classes. When this happens, the code technically uses objects, but it doesn’t follow the principles that make objects useful,so it ends up looking object‑oriented while lacking any real, well‑designed objects.

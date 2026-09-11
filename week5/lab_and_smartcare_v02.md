1. Problem Smart care wants a small, sustainable patient, practitioner and appointment system. As they currently use spreadsheets and paper records.This causes staff to duplicate bookings, difficulty finding patient information, inconsistent appointment status and limited appointment history. Assuming patients can also currently only make appointments by ringing up as there is no online booking system as they use spreadsheets. A simple small system that patients can book appointments in and clinic staff can manage practitioners appointments is required.
  

2. Stakeholders

Stakeholder                                                     
Patient                          

 Need          
To easily book appointments and be flexible with the times          

 Evidence
 Phone calls and feedback of patients wanting flexible times  


Stakeholder      
Practitioner            

Need      
To see patients previous appointment history and manage their billable time.    

Evidence
Clinic workflow requires reviewing past notes to help practitioners help understand the patient. Practitioners must be booked to optimum capacity to see the most patients in the time available.


Stakeholder 
Receptionist   

Need  
 Ways to quickly search up patients without facing any conflict. Easy way to find appointment availability and book free slots.

Evidence
Reception staff having difficulty finding patient files quickly. Difficulty in finding available time in booking and making duplicate bookings.


Stakeholder 
Clinic management 

Need  
Consistent reporting and management of the system  

Evidence
Management requires monthly performance and financial reports, booking maximum time for profitability. 



In scope
Patent record management 
Practitioner record management 
Appointment history 
Simple reporting for management
Small simple system operation
Booking appointments.
Search function.
  

OutScope  
EMR(electronic medical record)  functionality 
Unable to invoice,bill or payment processing  
Unable to record diagnosis prescriptions, medicine or treatment 

uncertain/provisional features 
Patient self service 
Email reminders 
Mobile app 
Inserting existing apps or features like medicare 

3. Functional Requirements
FR-01:The system should allow staff to update patients records when information changes on the patient e.g(home address)  
FR-02: the system should let staff search for patients using their description example name
FR-03: the system should let staff make new patient records 
FR-04: the system will block and prevent duplicate bookings  
FR-05: should allow staff to update appointment details example the time of the appointment 
FR-06: allow staff to cancel appointments 
FR-07: the system will show all details of an appointment on the system 
FR-08: the system should allow staff to create Practitioner records   
FR-09: the system should store and display a patient's appointment history 
FR-10: the system should allow staff to update Practitioner records when needed   
FR-11: the system should show a clean and completed appointment schedule for patient.
FR-12: the system should show and display a practitioners scheduled when needed 

4. Non-Functional Requirements
NFR-01: system Should load and display patient/practitioner records in very short time(3 seconds)
NFR-02: the system should be able to handle at least a dozen concurrent users with no performance issues 
NFR-03: the system needs to have a simple UI for everyone to understand 
NFR-04: the system will have user authentication and user roles to restrict access to sensitive user information 
NFR-05: the system will check all input fields to check that there is no empty or incorrect data  
NFR-06: the system should be inline and follow strict privacy laws 
NFR-07: the system can produce audit logs of use.

5. User Stories
US-01: As a patient, I want to book appointments online at any time so that I don't have to book in person or on the phone.
US-02: As a Receptionist , I want to update patient records, so that the patient's records are correct and up to date .
US-03: As a practitioner , I want to view past patient appointment history, so that I can understand the patient better.
US-04: As a Receptionist, I want to search a patient’s details quickly, so that there is no delay in retrieving information  .
US-05: As a practitioner, I want to update my availability , so that I can work with more patients and schedule my time .
US-06: As a Receptionist, I want to change appointment details , so that errors or incorrect data don’t occur.

6. Acceptance Criteria 
GIVEN a patient’s record exist’s 
WHEN  a Receptionist edits the details  
THEN the system will update and display with the new details 

GIVEN when Receptionist enters a patients name
WHEN the Receptionist uses the search function   
THEN the system shall display match patient records with the search description 

GIVEN  the appointment is made with missing required information (example patient) 
WHEN the Receptionist tries to upload the appointment
THEN an error happens and a  message pops up and shows “missing important information:

7. Assumptions and Open Question

Assumption 1
Receptionists and practitioners have basic computer literacy so there can understand and know how to use the system and what the system outputs is correct.

Assumption 2 
Smartcare has usable and reliable wifi and internet connectivity to operate and sustain the system with no problematic internet access issues  

Assumption 3 
Patients will provide correct and accurate information when booking an appointment and can produce relevant identity documentation if required.   


Open questions 
1. How long are the appointment time slots? 
2. Do patients need an account to book appointments?
3. Does the system need to support different types of appointments?
4. Are blocked out breaks required at certain times?
5. What are the hours of operation?
6. How do you label a practitioner as on leave or sick and do they get cancelled or do they get transferred to another practitioner.
7. Is printing required?
8. Does data have to be backed up?

AI Requirements Review and Verified :

AI Suggestion                                  Classification	                           Evidence Used 
Wi‑Fi reliability assumed                       Rejected                                  No evidence in requirements.
Staff computer skills assumed                   Rejected    No evidence in requirements. And all staff would already be adapted to using a laptop or a medical application. 

“Small, maintainable system” unclear             Modified                                 Scope mentions it but does not define it. 
Online booking conflicts with scope              Accepted                                 The user stories conflicts with the scope 
Duplicate booking rules missing                  Modified                               FR‑04 exists but doesn’t explain the duplicate bookings  
Appointment details missing                      Modified                               FR‑07 says “all details” but none listed. 


Reflection
What did AI notice that you missed? What did AI invent or overreach on? 
The AI identified important definitions that were not included, such as what counts as a “duplicate booking” , what “all appointment details” actually refer to and which fields belong in patient or practitioner records. These issues were present in the requirements but not explained so they were  ambiguous and open to interpretation. There was also an inconsistency in that online booking appears as a user story, yet the scope lists patient self service as only a provisional feature.
What AI invented or over reached on was a few points that went beyond what was written. For example the idea that staff might need training or that Wi‑Fi reliability could affect the system wasn’t supported anywhere in the requirements. Because there was no evidence for these they were treated as assumptions that need validation rather than confirmed problems.
The requirement that changed after the review was the online booking feature. At first it seemed valid because of US‑01 but once compared with the scope it became clear that this feature isn’t confirmed and needs clarification. Requirements need evidence to show they are correct and grounded in reality. 
Requirements must have evidence from real world stakeholders, derived from business value, and consider real world business workflows. This evidence can give legitimacy to the requirement. Without doing this requirements could be missed or overlooked or could be skewed based on just one stakeholders opinion. That's why requirements must be validated amongst a number of users and understood in light of the desired business outcomes and work flow.

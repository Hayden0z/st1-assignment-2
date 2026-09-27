A.Revisit Approved UML

Responsibilities 

Patient 
Store personal details example dob
Provide searchable patient information.
Allow staff to update patient records.
Provide appointment history to practitioners.


Practitioner 
Store practitioner details example dob
Provide availability for scheduling.
Allow staff to update practitioner records.
View patient history before appointments.


Appointment 
Store appointment details example date 
Link exactly one patient and one practitioner.
Prevent duplicate bookings.
Allow updates and cancellations.
Track appointment status example confirmed 


Attributes 
Patient attributes(name,patient_id,dob,gender)

Practitioner attributes (name,practitioner_id,dob,gender,area_specialty)

Appointment attributes(Appointment_id,date,time,type,room,status)



Relationships 

Relationship               Decision                                                    Rationale
Patient appointment       Composition                                            An appointment contains at least one reference to a patient.a patient is not a type of appointment so it would not work. one to many as patient can have many appointments but an appointment can only have one patient  

Practitioner appointment   Composition                                          An appointment contains at least one reference to practitioner.a practitioner is not a type of appointment so it would not work.one to many as practitioner can have many appointments but an appointment can only one practitioner   
  




B - Implement Patient:
class Patient:
    def __init__(self, patient_id: int, name: str, dob: str, gender: str):
        if type(patient_id) != int:
            raise ValueError("patient_id must be an integer")

        if name == "":
            raise ValueError("name cannot be empty")

        if dob == "":
            raise ValueError("dob cannot be empty")

        if gender == "":
            raise ValueError("gender cannot be empty")

        self.patient_id: int = patient_id
        self.name: str = name
        self.dob: str = dob
        self.gender: str = gender



C - Implement Practitioner with identifier, name and specialty

class Practitioner:
    def __init__(self, practitioner_id: int, name: str, area_specialty: str):
        if type(practitioner_id) != int:
            raise ValueError("practitioner_id must be an integer")

        if name == "":
            raise ValueError("name cannot be empty")

        if area_specialty == "":
            raise ValueError("area specialty cannot be empty")

        self.practitioner_id: int = practitioner_id
        self.name: str = name
        self.area_specialty: str = area_specialty



D.  Implement Appointment: Ai on 
class AppointmentError(Exception):
    pass

from enum import Enum

class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CONFIRMED = "confirmed"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Appointment:
    def __init__(self, appointment_id: int, date: str, time: str, room: str):
        if type(appointment_id) != int:
            raise AppointmentError("appointment_id must be an integer")

        If not date == "":
            raise AppointmentError("date cannot be empty")

        If not time == "":
            raise AppointmentError("time cannot be empty")

        If not  room == "":
            raise AppointmentError("room cannot be empty")

        self.appointment_id: int = appointment_id
        self.date: str = date
        self.time: str = time
        self.room: str = room

        self.status: AppointmentStatus = AppointmentStatus.SCHEDULED
        self.cancel_reason: str | None = None

    def confirm(self):
        if self.status == AppointmentStatus.CANCELLED:
            raise AppointmentError("Cannot confirm a cancelled appointment")

        if self.status == AppointmentStatus.COMPLETED:
            raise AppointmentError("Cannot confirm a completed appointment")

        if self._is_past():
            raise AppointmentError("Cannot confirm an appointment in the past")

        self.status = AppointmentStatus.CONFIRMED

    def cancel(self, reason: str = "No reason provided"):
        if reason == "":
            raise AppointmentError("Cancellation reason cannot be empty")

        self.status = AppointmentStatus.CANCELLED
        self.cancel_reason = reason

    def complete(self):
        if self.status != AppointmentStatus.CONFIRMED:
            raise AppointmentError("Only confirmed appointments can be completed")

        self.status = AppointmentStatus.COMPLETED

    def _is_past(self) -> bool:
        """
        Domain rule: appointments in the past cannot be confirmed.
        This is not visible in the UML but is a reasonable business constraint.
        """
        from datetime import datetime

        try:
            dt = datetime.strptime(f"{self.date} {self.time}", "%Y-%m-%d %H:%M")
        except ValueError:
            raise AppointmentError("Invalid date/time format, expected YYYY-MM-DD and HH:MM")

        return dt < datetime.now()

    def conflicts_with(self, other: "Appointment") -> bool:
        """
        Domain rule: two appointments conflict if they share the same room,
        date, and time. This is not shown in the UML but is a realistic constraint.
        """
        return (
            self.room == other.room and
            self.date == other.date and
            self.time == other.time and
            self.status != AppointmentStatus.CANCELLED and
            other.status != AppointmentStatus.CANCELLED
        )

EReview Generated Code
The AI generated Appointment code did not fully conform to the UML because it added unsupported features such as past date checks, conflict detection, custom exceptions and extra status values. These additions were not part of the approved design and made the class more complex than required.


 FManual Behaviour Checks
I checked that an Appointment can be created with valid details, and that wrong input like empty fields, or the wrong type causes an error. I cancelled a scheduled appointment to make sure the status changes correctly, and I tried an illegal action, like confirming a cancelled appointment, to see that the class blocked it. 


G Refactor the appointment code much more simpler and constituent with patient and practitioner
 from enum import Enum

from enum import Enum

class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

class Appointment:
    def __init__(self, appointment_id: int, date: str, time: str, room: str):
        if type(appointment_id) != int:
            raise ValueError("appointment_id must be an integer")
        if date == "":
            raise ValueError("date cannot be empty")
        if time == "":
            raise ValueError("time cannot be empty")
        if room == "":
            raise ValueError("room cannot be empty")

        self.appointment_id = appointment_id
        self.date = date
        self.time = time
        self.room = room
        self.status = AppointmentStatus.SCHEDULED

    def confirm(self):
        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError("Cannot confirm a cancelled appointment")
        self.status = AppointmentStatus.CONFIRMED

    def cancel(self):
        self.status = AppointmentStatus.CANCELLED

H
Is in smart care 




Reflection 
Which AI-generated part did you modify or reject? Why? How did the approved design constrain the AI?

I modified and rejected  the AI code for appointment because it added features that were not part of the approved design, such as past‑date checks, conflict detection and custom exceptions. The UML only required basic fields, simple validation and two status transitions, so the extra logic made the implementation harder than necessary. The approved design constrained the AI by limiting the class to the attributes and behaviours shown in the UML, which meant the final version had to stay simple, consistent, 

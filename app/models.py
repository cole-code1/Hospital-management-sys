from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

base = declarative_base()

class Doctors(base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    treatments = relationship("Treatment", back_populates="doctor")  # Relationship with Treatment
    appointments = relationship("Appointment", back_populates="doctor")  # Relationship with Appointment


class Patients(base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nhif_NO = Column(String)
    sickness = Column(String)

    treatments = relationship('Treatment', back_populates='patient')
    appointments = relationship("Appointment", back_populates="patient")  # Relationship with Appointment


class Treatment(base):
    __tablename__ = 'treatments'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    patient_id = Column(Integer, ForeignKey('patients.id'))  # Link treatment to patient

    patient = relationship('Patients', back_populates='treatments')
    doctor = relationship('Doctors', back_populates='treatments')


class Appointment(base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    appointment_date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)  # Status can be 'Scheduled', 'Completed', etc.

    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    patient_id = Column(Integer, ForeignKey('patients.id'))

    doctor = relationship('Doctors', back_populates='appointments')
    patient = relationship('Patients', back_populates='appointments')
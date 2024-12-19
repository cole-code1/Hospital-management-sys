from sqlalchemy import create_engine
# allows us to communicate with our database
from sqlalchemy.orm import sessionmaker
import os

from models import Doctors, Patients, Treatment, Appointment


engine = create_engine("sqlite:///hospital.sqlite")

#  create a session
session = sessionmaker(bind=engine)
session = session()
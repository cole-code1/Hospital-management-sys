from config import *


# Functions for CRUD Operations

def add_doctor():
    name = input("Enter Doctor Name: ")
    specialization = input("Enter Doctor's specialization: ")
    doctor = Doctors(name=name, specialization=specialization)
    session.add(doctor)
    session.commit()
    print("Doctor added successfully.")

def view_doctors():
    doctors = session.query(Doctors).all()
    for doctor in doctors:
        print(f"{doctor.id} - {doctor.name} - {doctor.specialization}")

def update_doctor():
    doctor_id = int(input("Enter doctor ID to update: "))
    doctor = session.query(Doctors).filter_by(id=doctor_id).first()
    if doctor:
        doctor.name = input(f"Enter new name (current: {doctor.name}): ")
        doctor.specialization = input(f"Enter new specialization (current: {doctor.specialization}): ")
        session.commit()
        print("Doctor updated successfully.")
    else:
        print("Doctor not found.")

def delete_doctor():
    doctor_id = int(input("Enter doctor ID to delete: "))
    doctor = session.query(Doctors).filter_by(id=doctor_id).first()
    if doctor:
        session.delete(doctor)
        session.commit()
        print("Doctor deleted successfully.")
    else:
        print("Doctor not found.")

# ====================Treatment=========================
def add_treatment():
    title = input("Enter Treatment Title: ")
    doctor_id = int(input("Enter Doctor ID: "))
    treatment = Treatment(title=title, doctor_id=doctor_id)
    session.add(treatment)
    session.commit()
    print("Treatment will undergo soon...please be patient")

def view_treatments():
    treatments = session.query(Treatment).all()
    for treatment in treatments:
        print(f"{treatment.id} - {treatment.title} - Doctor ID: {treatment.doctor_id}")

def update_treatment():
    treatment_id = int(input("Enter Treatment ID to update: "))
    treatment = session.query(Treatment).filter_by(id=treatment_id).first()
    if treatment:
        treatment.title = input(f"Enter new title (current: {treatment.title}): ")
        session.commit()
        print("Treatment updated successfully.")
    else:
        print("Treatment not found.")

def delete_treatment():
    treatment_id = int(input("Enter Treatment ID to delete: "))
    treatment = session.query(Treatment).filter_by(id=treatment_id).first()
    if treatment:
        session.delete(treatment)
        session.commit()
        print("Treatment deleted successfully.")
    else:
        print("Treatment not found.")

# ====================Patient=========================
def add_patient():
    name = input("Enter patient name: ")
    nhif_NO = input("Enter Patient NHIF_NO: ")
    sickness = input("Enter sickness: ")
    patient = Patients(name=name, nhif_NO=nhif_NO, sickness=sickness)
    session.add(patient)
    session.commit()
    print("Patient added successfully.")

def view_patients():
    patients = session.query(Patients).all()
    for patient in patients:
        print(f"{patient.id} - {patient.name} - {patient.nhif_NO} - {patient.sickness}")

def update_patient():
    patient_id = int(input("Enter Patient ID to update: "))
    patient = session.query(Patients).filter_by(id=patient_id).first()
    if patient:
        patient.name = input(f"Enter new name (current: {patient.name}): ")
        patient.nhif_NO = input(f"Enter new NHIF number (current: {patient.nhif_NO}): ")
        patient.sickness = input(f"Enter new sickness (current: {patient.sickness}): ")
        session.commit()
        print("Patient updated successfully.")
    else:
        print("Patient not found.")

def delete_patient():
    patient_id = int(input("Enter Patient ID to delete: "))
    patient = session.query(Patients).filter_by(id=patient_id).first()
    if patient:
        session.delete(patient)
        session.commit()
        print("Patient deleted successfully.")
    else:
        print("Patient not found.")

    # ====================Appointment=========================
def add_appointment():
    doctor_id = int(input("Enter Doctor ID: "))
    patient_id = int(input("Enter Patient ID: "))
    appointment_date = input("Enter Appointment Date and Time (YYYY-MM-DD HH:MM:SS): ")
    status = input("Enter Appointment Status (Scheduled/Completed): ")

    # Convert the appointment date string to a datetime object
    from datetime import datetime
    appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d %H:%M:%S")

    appointment = Appointment(
        doctor_id=doctor_id, 
        patient_id=patient_id, 
        appointment_date=appointment_date,
        status=status
    )
    session.add(appointment)
    session.commit()
    print("Appointment added successfully.")

def view_appointments():
    appointments = session.query(Appointment).all()
    for appointment in appointments:
        print(f"Appointment ID: {appointment.id} | Doctor ID: {appointment.doctor_id} | Patient ID: {appointment.patient_id} | Date: {appointment.appointment_date} | Status: {appointment.status}")

def update_appointment():
    appointment_id = int(input("Enter Appointment ID to update: "))
    appointment = session.query(Appointment).filter_by(id=appointment_id).first()
    if appointment:
        print(f"Current Appointment: Doctor ID: {appointment.doctor_id}, Patient ID: {appointment.patient_id}, Date: {appointment.appointment_date}, Status: {appointment.status}")
        appointment.status = input(f"Enter new status (current: {appointment.status}): ")
        appointment.appointment_date = input(f"Enter new appointment date (current: {appointment.appointment_date}): ")
        session.commit()
        print("Appointment updated successfully.")
    else:
        print("Appointment not found.")

def delete_appointment():
    appointment_id = int(input("Enter Appointment ID to delete: "))
    appointment = session.query(Appointment).filter_by(id=appointment_id).first()
    if appointment:
        session.delete(appointment)
        session.commit()
        print("Appointment deleted successfully.")
    else:
        print("Appointment not found.")


# ======================= Main CLI App ============================
def main():
    while True:
        os.system('clear')
        print("Welcome to Hospital Management System")
        print("1. Manage Doctors")
        print("2. Manage Treatments")
        print("3. Manage Patients")
        print("4. Manage Appointments")
        print("5. Exit")
        main_menu_choice = input("Enter your Choice: ")

        if main_menu_choice == '1':
            while True:
                os.system('clear')
                print("1. Add Doctor")
                print("2. View Doctors")
                print("3. Update Doctor")
                print("4. Delete Doctor")
                print("5. Back to Main Menu")
                doctor_menu_choice = input("Enter your Choice: ")
                if doctor_menu_choice == '1':
                    add_doctor()
                elif doctor_menu_choice == '2':
                    view_doctors()
                elif doctor_menu_choice == '3':
                    update_doctor()
                elif doctor_menu_choice == '4':
                    delete_doctor()
                elif doctor_menu_choice == '5':
                    break
                input("Press Enter to continue...")

        elif main_menu_choice == '2':
            while True:
                os.system('clear')
                print("1. Add Treatment")
                print("2. View Treatments")
                print("3. Update Treatment")
                print("4. Delete Treatment")
                print("5. Back to Main Menu")
                treatment_menu_choice = input("Enter your Choice: ")
                if treatment_menu_choice == '1':
                    add_treatment()
                elif treatment_menu_choice == '2':
                    view_treatments()
                elif treatment_menu_choice == '3':
                    update_treatment()
                elif treatment_menu_choice == '4':
                    delete_treatment()
                elif treatment_menu_choice == '5':
                    break
                input("Press Enter to continue...")

        elif main_menu_choice == '3':
            while True:
                os.system('clear')
                print("1. Add Patient")
                print("2. View Patients")
                print("3. Update Patient")
                print("4. Delete Patient")
                print("5. Back to Main Menu")
                patient_menu_choice = input("Enter your Choice: ")
                if patient_menu_choice == '1':
                    add_patient()
                elif patient_menu_choice == '2':
                    view_patients()
                elif patient_menu_choice == '3':
                    update_patient()
                elif patient_menu_choice == '4':
                    print("Thank you for o")
                    delete_patient()
                elif patient_menu_choice == '5':
                    break
                input("Press Enter to continue...")

        elif main_menu_choice == '4':
            while True:
                os.system('clear')
                print("1. Add Appointment")
                print("2. View Appointments")
                print("3. Update Appointment")
                print("4. Delete Appointment")
                print("5. Back to Main Menu")
                appointment_menu_choice = input("Enter your Choice: ")
                if appointment_menu_choice == '1':
                    add_appointment()
                elif appointment_menu_choice == '2':
                    view_appointments()
                elif appointment_menu_choice == '3':
                    update_appointment()
                elif appointment_menu_choice == '4':
                    delete_appointment()
                elif appointment_menu_choice == '5':
                    break
                input("Press Enter to continue...")

        elif main_menu_choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please choose again.")
            input("Press Enter to continue...")


# Call the main function
main()
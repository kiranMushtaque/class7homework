# 🏥 Hospital Management System – OOP in Python

This is a simple Object-Oriented Programming (OOP) based project written in Python to simulate a basic **Hospital Management System**. It was created as a homework assignment given by **Sir Ali Jawad** for class 7.

## 📌 Features

- Add and remove **Doctors**
- Add and remove **Patients**
- View lists of current doctors and patients
- Basic simulation of object relationships in a hospital system

## 🧠 Concepts Used

- Classes and Objects
- Constructors (`__init__`)
- Methods and Object manipulation
- Lists and basic data handling

## 🧪 Example Usage

```python
hospital = Hospital("City Hospital", "Lahore")

# Add doctors
doc1 = Doctor("Dr. Ali", "Cardiology")
hospital.add_doctor(doc1)

# Add patients
pat1 = Patient("Ahmed", "Flu")
hospital.add_patient(pat1)

# View all doctors and patients
print(hospital.get_doctors())  # ['Dr. Ali']
print(hospital.get_patients())  # ['Ahmed']

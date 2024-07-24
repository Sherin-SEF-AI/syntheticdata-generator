import sys
import pandas as pd
from faker import Faker
import random
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QComboBox, QCheckBox, QTextEdit, QPushButton,
                             QFileDialog, QMessageBox)

fake = Faker()

class DataGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Generator")
        self.setGeometry(100, 100, 600, 400)
        
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Data Type
        data_type_layout = QHBoxLayout()
        self.data_type_label = QLabel("Select Data Type:")
        self.data_type_combo = QComboBox()
        self.data_type_combo.addItems([
            "Personal Safety", "Industrial Worker Safety", "Industrial Safety",
            "Road Safety", "Vehicle Accident Data (Cars)",
            "Vehicle Accident Data (Two-Wheelers)", "Public Transportation Data"
        ])
        data_type_layout.addWidget(self.data_type_label)
        data_type_layout.addWidget(self.data_type_combo)
        layout.addLayout(data_type_layout)

        # Number of Records
        num_records_layout = QHBoxLayout()
        self.num_records_label = QLabel("Number of Records:")
        self.num_records_entry = QLineEdit()
        num_records_layout.addWidget(self.num_records_label)
        num_records_layout.addWidget(self.num_records_entry)
        layout.addLayout(num_records_layout)

        # Custom Parameters
        self.custom_params_check = QCheckBox("Include Custom Parameters")
        layout.addWidget(self.custom_params_check)

        self.custom_params_label = QLabel("Custom Parameters (key=value):")
        layout.addWidget(self.custom_params_label)
        self.custom_params_text = QTextEdit()
        layout.addWidget(self.custom_params_text)

        # Buttons
        self.open_params_button = QPushButton("Open Custom Params File")
        self.open_params_button.clicked.connect(self.open_custom_params)
        layout.addWidget(self.open_params_button)

        self.save_params_button = QPushButton("Save Custom Params")
        self.save_params_button.clicked.connect(self.save_custom_params)
        layout.addWidget(self.save_params_button)

        self.generate_button = QPushButton("Generate Data")
        self.generate_button.clicked.connect(self.on_generate)
        layout.addWidget(self.generate_button)

    def generate_data(self, data_type, num_records, **custom_params):
        data = []

        def get_custom_param(key, default=""):
            return custom_params.get(key, default)

        if data_type == "Personal Safety":
            incident_types = [
                "Theft", "Assault", "Burglary", "Vandalism", "Harassment",
                "Domestic Violence", "Cyberbullying", "Drug Abuse", "Fraud",
                "Hit and Run", "Kidnapping", "Riot", "Road Rage", "Robbery", "Sexual Assault"
            ]
            scenarios = {
                "Theft": ["Pickpocketing in a crowded market", "Car stolen from a parking lot", "Shoplifting in a retail store"],
                "Assault": ["Physical altercation at a bar", "Random attack on the street", "Domestic violence incident"],
                "Burglary": ["Breaking into a residential home", "Attempted break-in at an apartment", "Burglary at a garage"],
                "Vandalism": ["Graffiti on a public building", "Breaking car windows", "Damaging public park facilities"],
                "Harassment": ["Verbal abuse in a workplace", "Cyberbullying on social media", "Bullying in a school environment"],
                "Domestic Violence": ["Physical abuse by a partner", "Emotional abuse by a family member", "Financial control and exploitation"],
                "Cyberbullying": ["Hateful comments on social media", "Spreading false rumors online", "Threatening messages sent via email"],
                "Drug Abuse": ["Overdose in a public restroom", "Drug transaction observed at a party", "Possession of narcotics"],
                "Fraud": ["Online identity theft", "Phone scams targeting elderly", "Credit card fraud reported"],
                "Hit and Run": ["Driver flees after hitting a pedestrian", "Vehicle collision with another car and leaves the scene"],
                "Kidnapping": ["Abduction from a playground", "Hostage situation in a bank", "Forced entry into a vehicle at night"],
                "Riot": ["Protest turns violent", "Clashes between rival groups", "Public disturbance at a sporting event"],
                "Road Rage": ["Aggressive driving causing confrontation", "Intentional ramming of another vehicle", "Physical altercation after a traffic incident"],
                "Robbery": ["Mugging in an alley", "Armed robbery at a convenience store", "Home invasion and theft"],
                "Sexual Assault": ["Assault at a party", "Unwanted advances in public", "Attack during a jog in the park"]
            }

            for _ in range(num_records):
                incident_type = random.choice(list(scenarios.keys()))
                scenario = random.choice(scenarios[incident_type])
                
                record = {
                    "Name": fake.name(),
                    "Age": random.randint(18, 80),
                    "Gender": random.choice(["Male", "Female", "Non-binary"]),
                    "Location": get_custom_param("Location", fake.address()),
                    "Incident Type": incident_type,
                    "Scenario": scenario,
                    "Date": fake.date_this_year(),
                    "Time": fake.time(),
                    "Description": get_custom_param("Description", f"Incident: {scenario}. The situation involved {fake.word()} and resulted in {fake.word()}."),
                }
                data.append(record)

        elif data_type == "Industrial Worker Safety":
            incident_types = ["Slip and Fall", "Machinery Accident", "Chemical Exposure", "Fire", "Explosion"]
            descriptions = {
                "Slip and Fall": "Worker slipped on a wet surface and fell, causing minor injuries.",
                "Machinery Accident": "Accident involving malfunctioning machinery, resulting in injuries.",
                "Chemical Exposure": "Worker exposed to harmful chemicals leading to respiratory issues.",
                "Fire": "Fire outbreak in the facility due to faulty electrical wiring.",
                "Explosion": "Explosion occurred in the storage area due to improper handling of explosive materials."
            }
            for _ in range(num_records):
                incident_type = random.choice(incident_types)
                record = {
                    "Worker Name": fake.name(),
                    "Worker Age": random.randint(18, 65),
                    "Incident Type": incident_type,
                    "Location": get_custom_param("Location", fake.address()),
                    "Date": fake.date_this_year(),
                    "Time": fake.time(),
                    "Severity": random.choice(["Minor", "Moderate", "Severe", "Fatal"]),
                    "Description": descriptions[incident_type]
                }
                data.append(record)

        elif data_type == "Industrial Safety":
            incident_types = ["Equipment Failure", "Power Outage", "Gas Leak", "Fire", "Explosion"]
            descriptions = {
                "Equipment Failure": "Failure of critical equipment, causing a halt in production.",
                "Power Outage": "Unexpected power outage leading to operational delays.",
                "Gas Leak": "Gas leak in the facility requiring immediate evacuation.",
                "Fire": "Fire incident due to overheating of machinery.",
                "Explosion": "Explosion in the facility due to improper storage of hazardous materials."
            }
            for _ in range(num_records):
                incident_type = random.choice(incident_types)
                record = {
                    "Incident Type": incident_type,
                    "Location": get_custom_param("Location", fake.address()),
                    "Date": fake.date_this_year(),
                    "Time": fake.time(),
                    "Severity": random.choice(["Minor", "Moderate", "Severe", "Critical"]),
                    "Description": descriptions[incident_type]
                }
                data.append(record)

        elif data_type == "Road Safety":
            incident_types = ["Speeding", "Drunk Driving", "Reckless Driving", "Running Red Light", "Seatbelt Violation"]
            descriptions = {
                "Speeding": "Driver caught exceeding speed limits in a residential area.",
                "Drunk Driving": "Driver arrested for operating a vehicle under the influence of alcohol.",
                "Reckless Driving": "Driver engaged in dangerous maneuvers causing a traffic incident.",
                "Running Red Light": "Driver ignored traffic signals, resulting in a collision.",
                "Seatbelt Violation": "Driver fined for not wearing a seatbelt while driving."
            }
            for _ in range(num_records):
                incident_type = random.choice(incident_types)
                record = {
                    "Incident Type": incident_type,
                    "Location": get_custom_param("Location", fake.address()),
                    "Date": fake.date_this_year(),
                    "Time": fake.time(),
                    "Vehicle Type": random.choice(["Car", "Motorcycle", "Truck", "Bicycle"]),
                    "Severity": random.choice(["Minor", "Moderate", "Severe", "Fatal"]),
                    "Description": descriptions[incident_type]
                }
                data.append(record)

        elif data_type == "Vehicle Accident Data (Cars)":
            incident_types = ["Collision", "Hit and Run", "Roll Over", "Head-On Collision", "Rear-End Collision"]
            descriptions = {
                "Collision": "Vehicle involved in a collision with another vehicle or object.",
                "Hit and Run": "Driver fled the scene after causing an accident.",
                "Roll Over": "Vehicle rolled over due to loss of control.",
                "Head-On Collision": "Two vehicles collided head-on resulting in severe damage.",
                "Rear-End Collision": "One vehicle collided with the rear of another vehicle."
            }
            for _ in range(num_records):
                incident_type = random.choice(incident_types)
                record = {
                    "Vehicle Model": fake.word(),
                    "License Plate": fake.license_plate(),
                    "Incident Type": incident_type,
                    "Location": get_custom_param("Location", fake.address()),
                    "Date": fake.date_this_year(),
                    "Time": fake.time(),
                    "Severity": random.choice(["Minor", "Moderate", "Severe", "Fatal"]),
                    "Description": descriptions[incident_type]
                }
                data.append(record)

        elif data_type == "Vehicle Accident Data (Two-Wheelers)":
            incident_types = ["Collision", "Skidding", "Hit and Run", "Overtake Accident", "Road Defect"]
            descriptions = {
                "Collision": "Two two-wheelers collided with each other or another object.",
                "Skidding": "Two-wheeler skidded on a wet or uneven surface, causing an accident.",
                "Hit and Run": "Two-wheeler rider hit by a vehicle and the driver fled the scene.",
                "Overtake Accident": "Accident occurred while overtaking another vehicle.",
                "Road Defect": "Accident caused by defects or hazards on the road surface."
            }
            for _ in range(num_records):
                incident_type = random.choice(incident_types)
                record = {
                    "Vehicle Model": fake.word(),
                    "License Plate": fake.license_plate(),
                    "Incident Type": incident_type,
                    "Location": get_custom_param("Location", fake.address()),
                    "Date": fake.date_this_year(),
                    "Time": fake.time(),
                    "Severity": random.choice(["Minor", "Moderate", "Severe", "Fatal"]),
                    "Description": descriptions[incident_type]
                }
                data.append(record)

        elif data_type == "Public Transportation Data":
            incident_types = ["Bus Accident", "Train Collision", "Subway Incident", "Boat Accident", "Taxi Incident"]
            descriptions = {
                "Bus Accident": "Accident involving a public bus, causing delays and injuries.",
                "Train Collision": "Collision between trains or a train and another vehicle.",
                "Subway Incident": "Accident or incident occurring within a subway system.",
                "Boat Accident": "Accident involving a boat or ferry on a waterway.",
                "Taxi Incident": "Accident or incident involving a taxi cab."
            }
            for _ in range(num_records):
                incident_type = random.choice(incident_types)
                record = {
                    "Transportation Type": random.choice(["Bus", "Train", "Subway", "Boat", "Taxi"]),
                    "Incident Type": incident_type,
                    "Location": get_custom_param("Location", fake.address()),
                    "Date": fake.date_this_year(),
                    "Time": fake.time(),
                    "Severity": random.choice(["Minor", "Moderate", "Severe", "Fatal"]),
                    "Description": descriptions[incident_type]
                }
                data.append(record)

        return data

    def save_to_csv(self, data, file_path):
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)

    def on_generate(self):
        data_type = self.data_type_combo.currentText()
        num_records = int(self.num_records_entry.text())
        custom_params = {}
        if self.custom_params_check.isChecked():
            custom_params = dict(param.split('=') for param in self.custom_params_text.toPlainText().splitlines() if '=' in param)
        else:
            self.custom_params_text.setPlainText('')
        
        if not num_records:
            QMessageBox.warning(self, "Input Error", "Please enter the number of records.")
            return

        data = self.generate_data(data_type, num_records, **custom_params)
        
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if file_path:
            self.save_to_csv(data, file_path)
            QMessageBox.information(self, "Success", f"Data generated and saved to {file_path}")

    def open_custom_params(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Custom Parameters File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.custom_params_text.setPlainText(content)

    def save_custom_params(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Custom Parameters File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.custom_params_text.toPlainText())
            QMessageBox.information(self, "Success", f"Custom parameters saved to {file_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataGenerator()
    window.show()
    sys.exit(app.exec_())


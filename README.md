# syntheticdata-generator
GUI Python application for synthetic data generator 
Data Generator
Overview
The Data Generator application generates synthetic data for various types of incidents and scenarios. This data can be saved as a CSV file and is useful for testing, simulations, and analysis.

Features
Select Data Type: Choose from different data types such as Personal Safety, Industrial Safety, Road Safety, and more.
Number of Records: Specify the number of records to generate.
Custom Parameters: Include custom parameters for more detailed data.
Open and Save Custom Parameters: Load and save custom parameters from/to text files.
Generate Data: Create synthetic data based on the selected parameters and save it to a CSV file.
Requirements
To run this application, you'll need Python 3.x and the following packages:

PyQt5
Faker
pandas
You can install these dependencies using pip:

bash
Copy code
pip install PyQt5 faker pandas
Usage
Run the Application

Start the application by running the DataGenerator.py script:

bash
Copy code
python DataGenerator.py
Select Data Type

Choose the type of data you want to generate from the dropdown menu.

Enter Number of Records

Input the number of records you want to generate.

Include Custom Parameters

Check the box to include custom parameters.
Enter parameters in the format key=value in the text area, or use the "Open Custom Params File" button to load parameters from a file.
Generate Data

Click the "Generate Data" button to create the data. You'll be prompted to select a location to save the generated CSV file.

Open/Save Custom Parameters

Use the "Open Custom Params File" and "Save Custom Params" buttons to manage custom parameters.

Examples
Personal Safety Data: Generate records for incidents like theft, assault, or harassment.
Industrial Worker Safety Data: Create data for incidents involving industrial workers, such as machinery accidents or chemical exposures.
Road Safety Data: Produce data on road safety incidents, including speeding, drunk driving, and more.
Custom Parameters
Custom parameters allow you to add extra fields to the generated data. Parameters should be entered in key=value format. For example:

makefile
Copy code
Location=123 Elm Street
Description=Incident occurred at the corner of Elm Street and Maple Avenue.
File Formats
CSV Files: Generated data is saved in CSV format, compatible with spreadsheet software and data analysis tools.
Text Files: Custom parameters are saved in plain text format, with each parameter on a new line.

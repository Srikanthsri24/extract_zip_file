import zipfile
import os

# Define the path for extraction
extract_folder = "./data/student_management_system_extracted"

# Extract the ZIP file
with zipfile.ZipFile('./data/student_management_system.zip', 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

# List the files and directories in the extracted folder
os.listdir(extract_folder)

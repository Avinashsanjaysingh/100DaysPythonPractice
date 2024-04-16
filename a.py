import os

a = "day_0"

# Specify the base directory where you want to create the folders
base_directory = ""     # "path/to/your/directory" (to make more directories)

# Creating 100 folders named from 1 to 100
for i in range(100):
    b = a + str(i+1)
    folder_name = os.path.join(base_directory, (b))
    c = "notes_0" + str(i+1) + ".txt"
    # Checking if the folder already exists before creating it
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder '{i+1}' created successfully.")
        
        # Creating a test.py file in each folder
        with open(os.path.join(folder_name, c), 'w') as file:
            file.write("")
        
        print(f"File 'test.py' created in folder '{i+1}'.")
    else:
        print(f"Folder '{i+1}' already exists.")

# Note: Replace "path/to/your/directory" with the actual path where you want to create the folders.



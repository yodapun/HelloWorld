import os

directory = r"C:\Users\anshd\Desktop\Likeness"  # Replace with the actual directory path

counter = 1
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        name, number = filename.split(" ")
        name = name.upper()
        new_filename = f"3606_RM_RICKSHAW RELEASE_RICKSHAW {counter}_{number}_{name}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        counter += 1

#!/usr/bin/env python3.7

"""
A Python script that extracts information such as the name and size about the files 
in the current working directory and stores it in a list of dictionaries.
"""

import os  # OS module interacts with the operating system.
import os.path
import time # Time module enables working with time.

current_working_directory = os.getcwd() # Retrieves the absolute path of the current working directory ("pwd"). 

 # Option 1:  Retrieves the last part/basename of the absolute path of the current working directory.
 # Example:  "python-for-everything" is the basename for "/home/ec2-user/environment/python-for-everything."
tail = os.path.basename(current_working_directory)  

# Option 2:  Retrieves the absolute path of the current working directory
# and splits head (everthing up to the current working directory) and tail(current working directory).
#tail = os.path.split(os.getcwd()) 

current_directory_file_information = [] # Creates an empty list. 

print()
print("File information in your current working directory.") 
print()


for file in os.scandir(current_working_directory):  # List contents of the current working directory and returns os.DirEntry objects such as name, path, is_file.
    if file.is_file():
        
        file_name = file.name
        file_path = tail + '/' + file.name  # Concatenates current working directory and file name in the current working directory.
        file_size = os.stat(file_name).st_size # Retrieves the size of a file.
        modification_time = os.stat(file_name).st_mtime  # Retrieves the last modified date of a file
        
        # Create a list of dictionaries and append file information to the empty list. 
        file_information = {"name": file_name, "path": file_path, "size": file_size, "last modificationtime": modification_time}
        current_directory_file_information.append(file_information) # Appends file information to the list.
        
        # Prints below are optional.
        #print(file_information)
        #print()
        #print(current_directory_file_information)
        #print()
        
print(*current_directory_file_information,sep='\n') # Prints information in the "current directory file information" list. 
print()

        
        
        


        
        





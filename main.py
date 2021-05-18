import sys, os
from deletion.functions import get_files
from deletion.functions import delete_files
from command_line.functions import get_command_line_arguments

def main():
   
    path = types = ""
    
    # check if user has set a default starting directory and specified file 
    # types in the config file
    with open("config.txt", 'r') as f:
        for line in f:
            if line[0] is '#':
                continue
            if "dir=" in line and len(line) > 4:
                path = line[4:].strip()
            if "types=" in line and len(line) > 6:
                types = line[6:].strip() 
    f.close()

    # if there was no path provided in the configuration file set the defualt
    # path to directory where this main.py script is run from
    if path == "":
        path, _ = os.path.split(__file__)

    path, ctypes = get_command_line_arguments(path)
    
    # assign the value to types if the user provides a type through the 
    # command line
    if ctypes:
        types = ctypes
    
    # Allow user to view the files which are to be deleted
    working_files = get_files(path, types)
    
    if len(working_files) == 0:
        sys.exit("No files were found. Exiting program.")
    
    print("The following file copies have been selected for deletion:")
    for a_f in working_files:
        print(a_f)
    print()

    # Make sure user is ready to carry out the deletion
    while True:
        print("Do you wish to proceed with the deletion? (y/n): ", end = "")
        response = input()
        response = response.strip().upper()
        print()
        if response == 'Y':
            break
        elif response == 'N':
            sys.exit("User chooses to exit the program")

    # Delete the files in question
    delete_files(working_files)

if __name__ == '__main__':
    main()


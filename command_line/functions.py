import os, re, sys

def valid_path(path: str):
    '''
    Validates the directory path
    '''
    abs_path = os.path.abspath(os.path.normpath(path)) 
    try:
        if os.path.exists(abs_path):
            return abs_path
    except:
            return False



def get_command_line_arguments(default_path:str):
    '''
    Provides the command line user interface for the script. By default if no 
    directory or file types are provided this function will start to look for copies
    in the default_path provided by caller. If "--dir" followed by an 
    additional valid absolute or relative path is provided then the script will 
    start looking there. If "--types" is declared followed by a list of file
    extensions enclosed in quotation marks and separated by spaces. 
    Then the program will remove copies relating to those file types.
    '''
    if len(sys.argv) > 1 and sys.argv[1] not in ["--dir", "--types"]:
        sys.exit("Invalid program arguments")
    
    if len(sys.argv) > 3 and sys.argv[3] not in ["--dir", "--types"]:
        sys.exit("Invalid program arguments")

    if len(sys.argv) > 3 and sys.argv[1] == sys.argv[3]:
        sys.exit("Invalid program arguments")
  
    try:
        dir_i = sys.argv.index("--dir")
    except:
        dir_i = False

    try:
        type_i = sys.argv.index("--types")
    except:
        type_i = False
        
    if dir_i:
        try:
            working_path = valid_path(sys.argv[dir_i+1])
        
            if not working_path:
                raise Exception()
        except:
            sys.exit("Incorrect directory path was provided. Exiting program")
    else:
        working_path = valid_path(default_path)


    if type_i:
        try:
            file_type = list(set(sys.argv[type_i + 1].split(" ")))
        except:
            sys.exit("File types were not provided. Exiting program")

        for t in file_type:
            if re.search(r'[\s\\!<>\?\.,]', t):
                sys.exit(f"{t} is an invalid type format. Exiting program")
    else:
        file_type = None 
    
    return (working_path, file_type)
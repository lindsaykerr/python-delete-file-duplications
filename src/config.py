import os, re, sys

class Config:   

    def __init__(self, exec_location) -> None:
        self._path = ""
        self._types = []
        self._file = exec_location # takes __file__ object
        self._init_config()

    @property
    def path(self):
        return self._path

    @property
    def types(self):
        return self._types


    def _init_config(self):
        self._load_defaults_form_config_file()     
        if self._path_empty():
            self._path, _ = self._call_directory()
        self._assign_any_command_line_arguments()
        self._validate_path()
        self._validate_types()


    def _load_defaults_form_config_file(self):
        with open("config.txt", 'r') as f:
            
            for line in f:
                if line[0] == '#':
                    continue
                if "dir=" in line and len(line) > 4:
                    self._path = line[4:].strip()
                if "types=" in line and len(line) > 6:
                    self._types = line[6:].strip().split(" ")
        
        f.close()
    
    
    def _path_empty(self):
        return self._path == ""


    def _call_directory(self):
        return os.path.split(self._file)


    def _assign_any_command_line_arguments(self):    

        def argument_validation():
            if len(sys.argv) > 1 and sys.argv[1] not in ["--dir", "--types"]:
                sys.exit("Invalid program arguments")
            
            if len(sys.argv) > 3 and sys.argv[3] not in ["--dir", "--types"]:
                sys.exit("Invalid program arguments")

            if len(sys.argv) > 3 and sys.argv[1] == sys.argv[3]:
                sys.exit("Invalid program arguments")

        def assign_argument_values():
            # directory argument
            try:
                dir_arg = sys.argv.index("--dir")
            except:
                dir_arg = None   
            
            if dir_arg:
                try:
                    self._path = sys.argv[sys.argv.index("--dir")+1]
                except:
                    pass
            
            # types argument
            try:
                type_arg = sys.argv.index("--types")
            except:
                type_arg = None

            if type_arg:
                self._types = list(set(sys.argv[type_arg + 1].split(" ")))


        argument_validation()
        assign_argument_values()
    
    
    def _validate_path(self):
        abs_path = os.path.abspath(os.path.normpath(self._path)) 
        try:
            if os.path.exists(abs_path):
                self._path = abs_path
        except:
            sys.exit("Incorrect directory path was provided. Exiting program")

    
    def _validate_types(self):
        for type in self._types:
            if re.search(r'[\s\\!<>\?\.,]', type):
                sys.exit(f"{type} is an invalid type format. Exiting program")
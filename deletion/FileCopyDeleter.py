import re, os

class FileCopyDeleter:
    
    def __init__(self) -> None:
        self._deletion_list = []
        self._path = None
        self._file_types = ""

        self._regex_file_types = ""
        self._regex = None

    @property
    def path(self) :
        return self._path
    
    @path.setter
    def path(self, path: str) -> None:
        self._path = path

    @property
    def types(self):
        return self._file_types
    
    @types.setter
    def types(self, types_list):
        self._regex_set_file_types(types_list)
        self._file_types = ", ".join(types_list)
    
    @property
    def deletion_list(self):
        self._generate_deletion_list()    
        return self._deletion_list

    
    def _generate_deletion_list(self):
        self._deletion_list = []
        if (not self._path):
            raise RuntimeError("Failed to set properties path")
        
        self._reset_regex_for_searching()
        self._find_file_copies(os.path.normpath(self._path))
        return self._deletion_list


    def delete_copies(self):
        
        def execute():
            if not self._deletion_list:
                print("Nothing to delete")
                return

            for file_path in self._deletion_list:
                try:
                    os.remove(file_path)
                    print(file_path, "....deleted")
                except:
                    print(file_path, "....could not delete")
            
        
        print(f"Deleting ({len(self._deletion_list)}) files")
        execute()
        print("......Finished")

    
    # Private methods
    
    def _regex_set_file_types(self,file_types)-> str:
        if len(file_types) > 1:
            self._regex_file_types = "\\.(" + "|".join(file_types) + ")$"
        
        elif len(file_types) == 1:    
            self._regex_file_types = f'\\.{file_types[0]}$'
        
        else:
            self._regex_file_types = ""
    

    def _reset_regex_for_searching(self):
        regex_match_copy = r'(Copy|Copy ?\(\d+\)| \(\d+\)){}'
        self._regex = re.compile(regex_match_copy.format(self._regex_file_types))


    def _find_file_copies(self, path: str):    
        try:
            folder_items = os.scandir(path)   
        except: 
            return []
        self._copies_to_deletion_list(folder_items)

    
    def _copies_to_deletion_list(self, directory_items):
        
        def item_to_be_deleted():
            return self._regex.search(item.name[-15::])

        
        for item in directory_items:
            if item.is_dir():           
                self._find_file_copies(item.path)
            
            if item_to_be_deleted():
                self._deletion_list.append(item.path)
      
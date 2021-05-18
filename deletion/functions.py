import re, os

def get_files(start_path, a_type=None):
    '''
    Retrieves a list of directory and sub-directory files containing duplicate
    files. This function simply checks the file name and does not check the file
    size to determine if a copied file is a true copy.
    '''
    if isinstance(a_type, list):
        if len(a_type) > 1:
            a_type = "\\.(" + "|".join(a_type) + ")$"
        else:    
            a_type = f'\\.{a_type[0]}$'
    else:
        a_type = ""

    reg_copies = re.compile(r'(Copy|Copy ?\(\d+\)| \(\d+\)){}'.format(a_type))

    # inner helper, recursively searches sub directories and adds files
    # to a list 
    def _get_files(path: str):
        temp_list = []
        try:
            # get all the files and folders in a directory and process each one
            files = os.scandir(path)
            for file in files:
                # if we have a folder 
                if file.is_dir():   
                    # search for files in the sub folder         
                    temp_list.extend(_get_files(file.path))
                else: 
                    # it must be a file, check if it is a copy
                    if reg_copies.search(file.name[-15::]):
                        temp_list.append(file.path)
        except:
            # sometimes files are not accessible and scandir raises an error
            # so this try/exception allows us to skip such files. 
            pass
        return temp_list
    
    return _get_files(os.path.normpath(start_path))


def delete_files(removal_list)->None:
    '''
    Deletes a list of files with a valid path 
    '''
    print(f"Deleting ({len(removal_list)}) files")
    for a_file in removal_list:
        try:
            # simply removes file stated by the file path
            os.remove(a_file)
            print(a_file, "....deleted")
        except:
            print(a_file, "....could not delete")

import re, os

def get_deletion_list(start_path, file_type_list=[]):
    '''
    Retrieves a list of directory and sub-directory files containing duplicate
    files. This function simply checks the file name and does not check the file
    size to determine if a copied file is a true copy.
    '''
    def append_file_extentions(file_type_list: list)-> str:
        if len(file_type_list) > 1:
            return "\\.(" + "|".join(file_type_list) + ")$"
        
        if len(file_type_list) == 1:    
            return f'\\.{file_type_list[0]}$'
    
        return ""
    
    def regex_for_file_copies(file_type_list: list):

        return re.compile(
            r'(Copy|Copy ?\(\d+\)| \(\d+\)){}'
            .format(append_file_extentions(file_type_list))
            )


    def file_paths_to_list(folder_items, regex):
        
        def item_to_be_deleted():
            return regex.search(item.name[-15::])


        file_path_list = []

        for item in folder_items:
            if item.is_dir():           
                file_path_list.extend(items_for_deletion(item.path))
            else:            
                if item_to_be_deleted():
                    file_path_list.append(item.path)

        return file_path_list


    def items_for_deletion(path: str, regex):
        
        try:
            folder_items = os.scandir(path)   
        except: 
            return []
        
        return file_paths_to_list(folder_items, regex)
    
    regex = regex_for_file_copies(file_type_list)
    return items_for_deletion(os.path.normpath(start_path), regex)


def delete_file_copies(deletion_list: list)->None:
    '''
    Deletes a list of files with a valid path 
    '''
    print(f"Deleting ({len(deletion_list)}) files")
    
    for file_path in deletion_list:
        try:
            # simply removes file stated by the file path
            os.remove(file_path)
            print(file_path, "....deleted")
        except:
            print(file_path, "....could not delete")
    
    print("......Finished")
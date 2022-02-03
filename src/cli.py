from .abstractUI import AbstractUI
from .config import Config
import sys

class CommandLineInterface(AbstractUI):

    def __init__(self, config_obj: Config) -> None:
        super().__init__(config_obj)


    def print_deletion_list(self):
        deletion_list = self._deleter.deletion_list
        if len(deletion_list) == 0:
            sys.exit("No files were found. Exiting program.")
        
        print("The following file copies have been selected for deletion:")
        for deletion_item in deletion_list:
            print(deletion_item)
        print()


    def show_options(self):
        while True:
            print("Do you wish to proceed with the deletion? (y/n): ", end = "")
            response = input()
            response = response.strip().upper()
            print()
            if response == 'Y': 
                self._deleter.delete_copies()
                break
            if response == 'N': 
                sys.exit("Program exiting.")
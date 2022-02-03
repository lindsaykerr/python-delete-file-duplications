from src.config import Config
from src.cli import CommandLineInterface


def main():
    
    config = Config(__file__)
    interface = CommandLineInterface(config)
    interface.print_deletion_list()
    interface.show_options()
    

if __name__ == '__main__':
    main()


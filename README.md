# delete_dups.py
Python script for deleting file copies 

**WARNING!!! running this script can permanently delete files from your system. Run at your own risk! Ensure the generated listing of files queued for deletion by the program is reviewed before confirming deletion. When in doubt dont delete.**

The intended use for this script is in the case where large amounts of copies for a given file(s) has unintentionally occurred, and the user wants to remove these copies whilst leaving the original intact. To give an example I created this script because a client wanted to back-up their images on an external device, however on investigation I found that the size of their folder was extremely large with over 10 000 files. The images were being copied multiple times by some third party software which had been attempting to back-up the originals. So the user of the script, as is in case above, knows that the copies are identical and that they have a postfix of "Copy" or "Copy (_n_)" where _n_ is a number, or simply (n). The script does not perform any checks to determine if the original and presumed copy are identical. That is to say, if a file is copied and modified yet still retains the postfix identifiers of system copy, the script will still be added for deletion.

## Running the script
### Script arguments
The script by default, without command line arguments, will look for any files copies in the folder and sub-folders of the execution folder. Using the argument “--dir” followed by a valid directory path the user can search for copies in a specific location. For example:

`>python delete_dups.py –dir “C:\\Users\Auser\Home\Pictures”`

the user can also specify the file types which are to be deleted

`>python delete_dups.py –types “bmp jpg png”`

by simply separating the file formats with a space.

These two arguments can and should be used in conjunction to refine the process and are potentially safer as they are more targeted, prevented unintended files from being deleted.

### Using the Program
After the user runs the python script, the program scans the folder and respective subfolders. Then it will provide the user with a list of copies up for deletion. The user must then confirm that they wish to continue with the deletion by pressing on the keyboard “Y”. The program will then start deleting files, it will state that a file has been deleted. The program will then exit. If the user had chosen not to delete any files, the program will simply exit.

**NOTE: the files are permanently deleted you will not find them in your systems deletion bin/folder. Therefor it is important to ensure that you do wish to delete the files listed by the program. Deletions cannot be undone.** 

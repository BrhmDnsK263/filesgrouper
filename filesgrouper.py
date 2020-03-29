import os
from sys import argv, exit

"""Moves files in groups into folders.
Useful for dividing large numbers of files in the same directory
moving them into subfolders.

"filesgrouper.py [-h/--help]" for help.

"filesgrouper.py" to group files in the current directory

"filesgrouper.py [path]" to group files in the specified directory

"filesgrouper.py [number]" to group files in the current directory
                           in group of specified number of files

"filesgrouper.py [path] [number]" to group files in the specified directory
                                  in group of specified number of files
"""


#default config
default_path="."
default_quantity_group = 10
default_folder_base_name = "zzfolder"
default_folder_counter = 0
default_zerofill = 5

#help
help_message ="""
For help use "-h" or "--help"

"filesgrouper.py" to group files in the current directory

"filesgrouper.py [path]" to group files in the specified directory

"filesgrouper.py [number]" to group files in the current directory
                           in group of specified number of files

"filesgrouper.py [path] [number]" to group files in the specified directory
                                  in group of specified number of files
"""


def filesGroup(
        path=default_path,
        quantity_group=default_quantity_group,
        folder_base_name=default_folder_base_name,
        folder_counter=default_folder_counter,
        zerofill=default_zerofill
        ):
    """Moves files in groups into folders.

    Keyword arguments:
    path -- directory of the files to be moved
    quantity_group -- number of the max number of files in each group
    folder_base_name -- prefix for the name of the folders will be used
    folder_counter -- starting number to name each folder after prefix
    zerofill -- integer of how many zeros to fill the folder_counter
    """
    files = [
            file for file in os.listdir(path) 
            if (os.path.isfile(os.path.join(path,file)) and file != __file__)
            ]

    for index, item in enumerate(files):
        if(index%quantity_group == 0):          
            folder_name = folder_base_name + str(folder_counter).zfill(zerofill)
            new_folder_path = os.path.join(path,folder_name)
            folder_counter += 1
            
            if not os.path.exists(new_folder_path):
                print("creating folder: {}".format(folder_name))
                os.mkdir(new_folder_path)
            else:
                print("using existing folder: {}".format(folder_name))

        print("Moving file: {} to {}".format(item,new_folder_path))
        os.rename(os.path.join(path, item), os.path.join(new_folder_path, item))
        print("{} moved".format(item))

    print("Finish...")


if __name__ == "__main__":

    if len(argv) == 1:
        filesGroup()
        exit()

    if len(argv) > 1:
        for arg in argv:
            if arg == "-h" or arg == "--help":
                print(help_message)
                exit()

    if len(argv) == 2:
        if os.path.isdir(argv[1]):
            default_path = argv[1]
        else:
            try:
                 default_quantity_group = int(argv[1])
                 
            except:
                print(help_message)
                exit()

    if len(argv) == 3:
        if os.path.isdir(argv[1]):
            default_path = argv[1]
        else:
            print(help_message)
            exit()          
        try:
                 default_quantity_group = int(argv[2])               
        except:
            print(help_message)
            exit()

    filesGroup(
            path=default_path,
            quantity_group=default_quantity_group,
            folder_base_name=default_folder_base_name,
            folder_counter=default_contador_carpeta,
            zerofill=default_zerofill
            )
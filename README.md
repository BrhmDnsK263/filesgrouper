# FilesGrouper

Moves files in groups into folders.

Utility for moving files in groups into folders with a max number of files in each group.

Useful for dividing large groups of files that slow down some file managers moving them into subfolders.


## Usage

For help:
```bash
filesgrouper.py [-h/--help]
```
To group files in the current directory
```bash
filesgrouper.py
```
To group files in the specified directory
```bash
filesgrouper.py [path]
```
To group files in the current directory in group of specified number of files
```bash
filesgrouper.py [number]
```
to group files in the specified directory in group of specified number of files
```bash
filesgrouper.py [path] [number]
```


## Usage from another script

```python
from filesgrouper import filesGroup

filesGroup(
		path,
		quantity_group,
		folder_base_name,
		folder_counter,
		zerofill
		):
```


Keyword arguments:
```
path -- directory of the files to be moved.
quantity_group -- number of the max number of files in each group.
folder_base_name -- prefix for the name of the folders will be used.
folder_counter -- starting number to name each folder after prefix.
zerofill -- integer of how many zeros to fill the folder_counter.
```

## Built With

* Python3
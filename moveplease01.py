#!/usr/bin/env python3

# import shutil. This import statement reminds Python to bring special tools (modules) to the jobsite (our script). 
import shutil

# Import the os module; os module provides a portable way to use operating system dependent functionality. Shutil allows higher-level file manipulation, os is more targeted at the operating system. 
import os

# Makes Python start in the home user directory
os.chdir('/home/student/mycode/')


# Moves the file or folder at the path source to the path destination and returns a string of the absolute path of the new location. If destination points to a folder, the source file gets moved into destination and keeps its current filename. 
shutil.move('raynor.obj', 'ceph_storage/')

# Prompts the user for a new name for  the kerrigan.obj file.
xname = input('What is the new name for kerrigan.obj? ')

# Rename the current kerrigan.obj file. 
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


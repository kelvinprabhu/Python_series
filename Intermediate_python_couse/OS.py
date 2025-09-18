# module os in python - it is used to interact with the operating system
import os
print(dir(os))  # it will print all the functions and attributes available in os module
print(os.getcwd())  # it will print the current working directory
# os.chdir("path")  # it will change the current working directory to the specified path
# os.mkdir("path")  # it will create a new directory at the specified path
# os.makedirs("path")  # it will create a new directory and all intermediate directories at the specified path
# os.rmdir("path")  # it will remove the specified directory
# os.removedirs("path")  # it will remove the specified directory and all intermediate
# os.rename("old_name", "new_name")  # it will rename a file or directory
# os.listdir("path")  # it will list all files and directories in the specified path
# os.stat("path")  # it will return the status of the specified file or directory
# os.walk("path")  # it will generate the file names in a directory tree by walking the tree either top-down or bottom-up
# os.environ  # it will return a dictionary of environment variables
# os.path  # it is a submodule of os module that is used
# to manipulate file and directory paths
print(os.path)  # it will print the os.path module
print(os.path.basename("Advance_python_couse/OS.py"))  # it will print the base name of the file
print(os.path.dirname("Advance_python_couse/OS.py"))  # it will print the directory name of the file
print(os.path.join("Advance_python_couse", "OS.py"))  # it will join
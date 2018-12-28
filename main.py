import os
path =str(input("Insert the path to the file that you want to convert "))
command = "soffice --headless --convert-to pdf " + path
os.system(command)
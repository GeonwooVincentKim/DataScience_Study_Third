import os
import sys

import os.path
saveFileLocation = sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

if os.path.isfile(saveFileLocation):
    print("Confirm file exist")
elif os.path.isdir(saveFileLocation):
    print("Confirm file directory")


file_for_reading = open("reading_file.txt", 'r')
file_for_reading2 = open("reading_file.txt")

file_for_writing = open("writing_File.txt", "w")


file =open("OwnModule.py","r")
print(file.read())
file.close()
# r, w, a, r+, w+, a+

file =open("OwnModule.py","w")
file.write("# how are you ? ")
file.close()

#file methods
#open()  : To open the file
#  close() : To close the file
# read()   :returns the file content
#  write() : write text to file
#readline() : return line of text
#  writeline() : writes line of text
#readlines()  :return list of lines
#  writelines() : writes list of lines to file
#readable() : returns whether readable or not?
#  writable() : returns whether writable or not?
#tell()      :returns the current file position()
# truncate() : resize the file
#seek()      :change the file position
# seekable() :Whether allowed to change the file position.
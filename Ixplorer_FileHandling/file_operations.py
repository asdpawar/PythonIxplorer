###########################################################################################################################
# read the file
read_content = file1.read()
print(read_content)

# close the file
file1.close()

###########################################################################################################################

# with open syntax which closes file automatically   (read)
with open("test.txt", "r") as file1:
    read_content = file1.read()
    print(read_content)

    
###########################################################################################################################
    
# with open syntax which closes file automatically   (write)
with open(test2.txt', 'w') as file2:
    # write contents to the test2.txt file
    file2.write('Programming is Fun.')
    fil2.write('Programiz for beginners')
          
###########################################################################################################################
          
#exception handling
try:
    file1 = open("test.txt", "r")
    read_content = file1.read()
    print(read_content)

finally:
    # close the file
    file1.close()
    
###########################################################################################################################          
file1 = open("test.txt", "r")

file1 = open("test.txt", "t") # opens in default text mode

file1 = open("test.txt")      # equivalent to 'r' or 'rt'

file1 = open("test.txt",'w')  # write in text mode, creates file in case file doesn't exist

file1 = open("test.txt", "b") # opens in binary mode

file1 = open("img.bmp",'r+b') # read and write in binary mode

file1 = open("test.txt",'w')  # write in text mode

file1 = open("test.txt", "x") # opens for exclusive creation, fails if already exist

file1 = open("test.txt", "a") # appending at the end of the file, creates if doesn't exist

###########################################################################################################################
          

close()          # Closes an opened file. It has no effect if the file is already closed.
			
detach()         # Separates the underlying binary buffer from the TextIOBase and returns it.
			 
fileno()         # Returns an integer number (file descriptor) of the file.
			     
flush()          # Flushes the write buffer of the file stream.
			
isatty()         # eturns True if the file stream is interactive.
			
read(n)          # Reads at most n characters from the file. Reads till end of file if it is negative or None.
			  
readable()       # Returns True if the file stream can be read from.
			
readline(n=-1)   # Reads and returns one line from the file. Reads in at most n bytes if specified.
			
readlines(n=-1)  # Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
			
seek(offset,from=SEEK_SET)         # Changes the file position to offset bytes, in reference to from (start, current, end).
			
seekable()       # Returns True if the file stream supports random access.
			
tell()           #  Returns an integer that represents the current position of the file's object.
			
truncate(size=None)                # Resizes the file stream to size bytes. If size is not specified, resizes to current location.
			
writable()       # Returns True if the file stream can be written to.
			
write(s)         # Writes the string s to the file and returns the number of characters written.
			
writelines(lines)                  # Writes a list of lines to the file.

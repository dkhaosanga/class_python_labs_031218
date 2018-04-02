# file = open('file.txt', 'r', encoding='utf-8')
# #first put in the file path location of where THIS (file.txt) is , second - what do you want the file to do?  write, read, appending if the file already exsist and write at the end of the file, etc.
#
# text = file.read()
# print(text)
# file.close()
#
###format to use
# with open('file.txt', 'r') as file:
#'file' about can be anything, only within THIS scope
    # text = file.read()
#text is global scope
#
#printing all of the text in file
# print(text)
#file.readlines()
#
#to open files in a different directory that's not in the same directory as your files
#cd to the file directory in the comand line (to find) file path to where you're at relative to currenly
#
#
# with open ('file.txt', 'r') as file:
#     text_lines = file.readlines()
#read lines is split on character lines
#print(text_lines)
#
# for i in lines:
#     print (i)
# #this prints a line between because it's irritating each line in the line, but it has print so it's preting the extra line
#
# #   print (i, ends='')    to get rid of those extra lines

#when you write 'w' and the file is not there it will create a new files, ie if 'file.txt' was actually 'example.txt'
#'w' and then the next line 'a' to add on the file, 'a' - appending will copy and add to whatever was there previously
# don't forget to add the character line \n within the ('I love ruby! \n') if you want the text to be on another line

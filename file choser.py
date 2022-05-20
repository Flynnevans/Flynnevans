#https://pynative.com/python/file-handling/#:~:text=Python%20File%20Methods%20%20%20%20Method%20%2ca%20specified%20size.%20%207%20more%20rows%20
#site with all of the file handling
import os.path
def create_file(text):
    with open("test.txt", "w") as fp:
        fp.write(text)
#creates file with text in

def file_exist(filepath):
    if os.path.exists(filepath):
        return(true)
#checks if the file exists


def file_size(filepath):
    return(os.path.getsize(filepath))
#returns the file size in bytes

def line_counter(filepath):
    with open(filepath, 'r') as fp:
        for count, line in enumerate(fp):
            pass
    return( count + 1)
#returnes the amount of lines

def specific_line(filepath,hi):
    with open(filepath, 'r') as fp:

        line_numbers = [hi]

        lines = []
        for i, line in enumerate(fp):

            if i in line_numbers:
                lines.append(line.strip())
            elif i > hi:

                break
    return(lines)

#returns the specific line that you want


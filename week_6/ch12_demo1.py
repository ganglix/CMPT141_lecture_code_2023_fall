# Read in the file data to create dictionary extensions that
# maps extension numbers to employees
# .txt
# .csv  comma-separated values

# open
# absolute path: full directory
# path = "V:\Desktop\CMPT141_lecture_code_2023_fall\week_6\ext_directory_data.txt"

# relative path
path = "ext_directory_data.txt" # by default find it in the current folder
# . means current directory or folder
# .. means the parent directory or folder

# path = "./ext_directory_data.txt"
# path = "../week_6/ext_directory_data.txt"


f = open(path, "r")  # permission to read, read mode, f is the file object
extensions = {}  # number: name
for line in f:
    # print(line) # at the end of the line, there is a newline "\n" invisible sign
    # print(line.rstrip())   # use rstrip() to remove that trailing "\n"
    line_parse = line.rstrip().split(",")  # return a list of substrings splitted by ,
    number = int(line_parse[0])
    name = line_parse[1]
    extensions[number] = name

# dont forget to close it
f.close()

print(extensions)
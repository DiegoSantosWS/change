import os, re

pathFile = '<PATH>/<NAME_PROJECT>'
directorys = os.listdir()
total = 0
def listDirectorys(directory):
    tot = 0
    if os.path.isdir(directory):
        items = os.listdir(directory)
        if directory == ".git":
            return 0
        for file in items:
            strs = pathFile+directory+'/'+file
            open_file = open(strs,'r')
            read_file = open_file.read()
            regex = re.compile('<name_old>')
            read_file = regex.sub('<new_name>', read_file)
            write_file = open(strs,'w')
            write_file.write(read_file)    
            tot += 1
    return tot

if __name__ == '__main__':
    for directory in directorys:
        total += listDirectorys(directory)
    print("Total de arquivos: " + str(total))
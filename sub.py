import os, re

directory = os.listdir('/home/diegos/projetos/src/github.com/DiegoSantosWS/change/')
os.chdir('/home/diegos/projetos/src/github.com/DiegoSantosWS/change/')

for file in directory:
    open_file = open(file,'r')
    read_file = open_file.read()
    print(read_file)
    regex = re.compile('diego')
    read_file = regex.sub('errors', read_file)
    write_file = open(file,'w')
    write_file.write(read_file)


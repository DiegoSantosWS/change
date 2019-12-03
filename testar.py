import os, re

pathFile = '<PATH>/<NAME_PROJECT>'
pastas = os.listdir()
total = 0
def listarArquivos(pasta):
    tot = 0
    if os.path.isdir(pasta):
        items = os.listdir(pasta)
        if pasta == ".git":
            return 0
        for file in items:
            strs = pathFile+pasta+'/'+file
            print("item ", file)
            open_file = open(strs,'r')
            read_file = open_file.read()
            regex = re.compile('<name_old>')
            read_file = regex.sub('<new_name>', read_file)
            write_file = open(strs,'w')
            write_file.write(read_file)    
            tot += 1
    return tot

if __name__ == '__main__':
    for pasta in pastas:
        total += listarArquivos(pasta)
    print("Total de arquivos: " + str(total))
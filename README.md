# SUBISTITUINDO PALAVRAS

```bash
change $: cd change

change $: cp testar.py /project
```

abre o aquivo testar.py e altera o path para caminho real /home ...

alterar o compile e sub come no exemplo

```py

regex = re.compile('<name_old>')
read_file = regex.sub('<new_name>', read_file)

regex = re.compile('gitlab.com/diegosantos') #de gitlab.com/name-user-company
read_file = regex.sub('github.com/DiegoSantosWS', read_file) # para github.com/name-user-company
```

no terminal...

```bash
your-project $: python3 testar.py
```

após conferir basta executar o comando para remover o arquivo ```rm testar.py``` do diretorio atual repita o mesmo processo em todos os outros diretorios que necessita da mudança

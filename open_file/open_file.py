import os

#mostrar os arquivos no diretório corrente - leia-se: diretório em q se encontra no terminal
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))


# acessar um arquivo
# 1º arg - caminho do arquivo, se na mesma pasta só informar nome do arquivo com a extensão. Referencia é o terminal.
# como enquanto faço este estudo o terminal se encontra na pasta raiz 
# adicionei ao argumento o path do cwd até o arquivo de exemplo
# 2º arg:
# "r" - read
# "r+" - read / write ???
# "w" - write
# "a" - append - adicionar informação ao final do arquivo
read_file = open("open_file/example.txt","r") 

# readable() - retorna boolean - se o arquivo é possível ser lido.
print(read_file.readable())
# Sempre lembrar de fechar o arquivo
read_file.close()


read_file = open("open_file/example.txt","r") 
# read() - retorna o conteúdo do arquivo. move o cursor para o fim do arquivo
print(read_file.read())
# Sempre lembrar de fechar o arquivo
read_file.close()


read_file = open("open_file/example.txt","r") 
# readline() - retorna conteúdo de uma linha e move o cursor para a próxima
print(read_file.readline())
print(read_file.readline())
print(read_file.readline())
# Sempre lembrar de fechar o arquivo
read_file.close()


read_file = open("open_file/example.txt","r") 
# readlines() - retorna o conteúdo do arquivo em uma lista a partir do cursor, onde cada linha é um elemento do array
# se o cursor estiver no final do arquivo retorna uma lista vazia
print(read_file.readlines())
# Sempre lembrar de fechar o arquivo
read_file.close()


read_file = open("open_file/example.txt","r") 
# retorna o conteudo da linha daquele index especifico.
print(read_file.readlines()[0])
# Sempre lembrar de fechar o arquivo
read_file.close()



# append

append_file = open("open_file/example.txt","a")
# adiciona conteudo ao arquivo
# \n - adiciona o conteudo em uma nova linha
append_file.write("\nnovo conteudo no arquivo")
# Sempre lembrar de fechar o arquivo
append_file.close()





# write

write_file = open("open_file/example.txt","w")
# reescreve o conteúdo do arquivo, 
# vá até o arquivo examples edite e rode o script,
# acesse o arquivo novamente e veja o novo conteúdo
write_file.write("Conteúdo original do arquivo foi embora. \neste é o novo conteúdo agora.")
# Sempre lembrar de fechar o arquivo
write_file.close()

# se o arquivo não for encontrado no caso do 2º arg ser "w" (write), um novo arquivo será criado.
new_file = open("open_file/cars.txt", "w")
new_file.write("Argo - Fiat\nGol - Volkswagen\nOnix - Chevrolet")
# Sempre lembrar de fechar o arquivo
new_file.close()

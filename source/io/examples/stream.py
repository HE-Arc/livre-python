#Programme qui écrit les 10 premiers caractères du fichier input.txt dans le fichier output.txt

try:
    inputStream = open("input.txt",mode='r')

    outputStream = open("output.txt",mode='w') #Crée le fichier output si il n'existe pas

    if inputStream.readable() and outputStream.writable():
        outputStream.write(inputStream.read(10))
    else:
        print("Un problème a eu lieu.")

    inputStream.close()
    outputStream.close()
except:
    print("Fichier de lecture non trouvé.")

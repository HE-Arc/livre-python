try:
    with open('input.txt', 'r') as is, :
        with open('output.txt', 'w') as os:
            os.write(is.read(10))
except PermissionError:
    #...
except OSError:
    #...

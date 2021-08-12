import itertools

string = input("Strings para combinar")

result =  itertools.permutations(string, len(string))

for i in result:
    print(''.join(i))
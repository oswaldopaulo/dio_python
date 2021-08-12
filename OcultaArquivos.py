import ctypes

pasta = input("Caminho da pasta ex C:/pasta")
att_hidden = 0x02
retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, att_hidden)

if retorno:
    print("Arquivo oculto")
else:
    print("Não consegui")
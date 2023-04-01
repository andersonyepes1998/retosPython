usuario=input('Digitalice un nombre del usuario: ')
contraseña=input('Digitalice una contraseña: ')
inicios = 0
retorno = True
def validarUsuario(usuario, contraseña):
    if usuario == ('admin') and contraseña == ('admin123*'):
        print('Verdadero...')
        return True
    
    else:
        print('Incorrecto...')
        return False
retorno  = validarUsuario(usuario,contraseña)

while(retorno == False):
    inicios = int(inicios + 1)
    print(inicios)
    usuario=input('Digitalice un nombre del usuario: ')
    contraseña=input('Digitalice una contraseña: ')
    retorno  = validarUsuario(usuario,contraseña)

        

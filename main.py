import os
import time
import random

from Menu import menu_seleccion

#Imagen de titulo
titulo = """
 __      __                _____                 _   ______                             _   _             
 \ \    / /               / ____|               | | |  ____|                           | | (_)            
  \ \  / ___ _ __ _   _  | |  __  ___   ___   __| | | |__   _ __   ___ _ __ _   _ _ __ | |_ _  ___  _ __  
   \ \/ / _ | '__| | | | | | |_ |/ _ \ / _ \ / _` | |  __| | '_ \ / __| '__| | | | '_ \| __| |/ _ \| '_ \ 
    \  |  __| |  | |_| | | |__| | (_) | (_) | (_| | | |____| | | | (__| |  | |_| | |_) | |_| | (_) | | | |
     \/ \___|_|   \__, |  \_____|\___/ \___/ \__,_| |______|_| |_|\___|_|   \__, | .__/ \__|_|\___/|_| |_|
                   __/ |                                                     __/ | |                      
                  |___/                                                     |___/|_|                      
""" # https://patorjk.com/

#Clase de encriptado
#O(n)
class cypher:
    def __init__(self, text):
        hex = "123456789ABCDEF" #String con los posibles valores hexadecimales
        self.chars = "" #String encriptado
        self.key = ""  #Llave de encriptacion

        for i in text:
            rand = random.randint(0, 14) #Crea un valor random hexadecimal
            
            hexVal = hex[rand] #Busca el valor hexadecimal en el string

            #1. Convierte el valor i del texto a su valor ascii
            #2. Le suma su valor hexadecimal respectivo
            #3. Convierte el valor a un caracter
            txt = ord(i) + rand

            if(txt > 126): #En caso de que txt sea mayor a 126 (limite de ascii)
                txt = 32 + (txt - 126) #Checa por cuanto se paso, lo lleva al primer valor de ascii y le suma la diferencia

            #4. Lo agrega al string chrs
            self.chars += chr(txt)

            self.key += hexVal #Agrega el valor hex a la llave


#Clase de decriptado
#O(n)
class plainText:
    def __init__(self, cypher, key):
        self.pTxt = "" #Texto decriptado
        
        for i in range(len(key)):
            intVal = int(key[i], 16) #Convierte el valor hexadecimal de la llave a su valor decimal

            txt = ord(cypher[i]) - intVal + 1 #Convierte el valor del texto a ascii y realiza la operacion de acuerdo al valor de la llave

            if(txt < 32): #En caso de que el valor sea menor a 32 (limite ascii)
                txt = 126 - (32 - txt) #Lo convierte a 126 y le resta la diferencia

            self.pTxt += chr(txt) #Agrega al string decriptado el caracter


#Menu de encriptado
def menuEncri():
    os.system('cls') #limpia la consola

    print('Como se llama el archivo que quieres encriptar?')

    try:
        file = open(input(), 'r') #Intenta recivir un archivo
    except: #Si el archivo no existe se le dice al usuario y se llama a si misma la funcion
        print('No se encontro ese archivo')
        time.sleep(2)
        menuEncri()

    c = cypher(file.read()) #Lee el texto del archivo y lo manda a la clase cypher
    file.close() #Cierra el archivo para conservar memoria

    print('Tu cifrado se encuentra en el archivo cypher.txt')
    print('Tu llave se encuentra en el archivo key.txt')

    if os.path.exists("cypher.txt"): #Busca si el archivo existe
        os.remove("cypher.txt") #Lo borra en caso de que si exista

    cy = open('cypher.txt', 'x') #Crea el archivo
    cy.write(c.chars) #Escribe el texto encripatado en el archivo
    cy.close() #cierra el archivo para conservar memoria

    if os.path.exists("key.txt"): #Busca si el archivo existe
        os.remove("key.txt") #Lo borra en caso de que si exista

    ky = open('key.txt', 'x') #Crea el archivo
    ky.write(c.key) #Escribe la llave en el archivo
    ky.close() #cierra el archivo para conservar memoria

    print('\nPresiona cualquier tecla para regresar al menu principal')
    input()

    menu() #Te manda de regreso al menu principal


#Menu de decriptado
def menuDecri():
    os.system('cls') #Borra la consola

    print('Como se llama el archivo que quieres decriptar?')
    
    try: #Intenta recivir un archivo
        cyph = open(input(), 'r')
    except: #Si no lo recive se llama a si misma
        print('Ese archivo no existe')
        time.sleep(2)
        menuDecri()

    print('Como se llama tu archivo con la llave?')

    try: #Intenta recivir un archivo
        key = open(input(), 'r')
    except: #Si no lo recive se llama a si misma
        print('Ese archivo no existe')
        time.sleep(2)
        menuDecri()

    pt = plainText(cyph.read(), key.read()) #Crea el objeto

    #Cierra los archivos para conservar memoria
    cyph.close()
    key.close()

    if os.path.exists("plainText.txt"): #Busca si el archivo existe
        os.remove("plainText.txt") #Lo borra en caso de que si exista

    pText = open('plainText.txt', 'x') #Crea el archivo
    pText.write(pt.pTxt) #Escribe el mensaje decriptado en el
    pText.close() #Lo cierra

    print('Tu decripcion se encuentra en el archivo plainText.txt')

    print('\nPresiona cualquier tecla para regresar al menu principal')
    input()

    menu() #Te manda de regreso al menu principal


#Menu principal
def menu():
    os.system('cls')

    titulo_width = len(max(titulo.splitlines())) #Tamano del ancho del titulo para centrar el menu

    print(titulo) #Imprime el menu

    print('>Opciones<\n'.center(titulo_width)) 
    options = [
        'Encriptar', #Opcion para encriptar un archivo
        'Decriptar', #Opcion Para decriptar un archivo
        'Exit' #Opcion para salir del programa
    ]

    options = [opt.center(titulo_width) for opt in options] #Lista de las opciones
    choice = menu_seleccion(options).strip() #Se mandan a imprimir las opciones y se regresa un valor string

    if choice == 'Encriptar':
        menuEncri()

    elif choice == 'Decriptar':
        menuDecri()

    elif choice == 'Exit':
        exit()


menu()
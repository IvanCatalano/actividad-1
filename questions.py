import random
dic = {
   '1' : [
        "python",
        "programa",
        "variable",
        "funcion",
        "bucle",
        "cadena",
        "entero",
        "lista"
        ] ,
    '2' : [
       "rojo", "azul", "verde", "amarillo", "naranja", "violeta", "negro", "blanco"
    ] ,
    '3' : [
       "argentina", "brasil", "chile", "uruguay", "paraguay", "bolivia", "peru", "colombia"
    ]
    }
while True :
    print('Categorias disponibles : \n1 : "Programacion"\n2 : "Colores"\n3 : "Paises"')
    seleccion = input('Seleccione el numero de la categoria que quiera jugar : ')
    if not seleccion.isdigit() or int(seleccion) < 1 or int(seleccion) > 3:
       print('El numero esta fuera de las categorias disponibles')
    else :
       break
lista_palabras = random.sample(dic[seleccion], len(dic[seleccion]))
while len(lista_palabras) != 0 :
    print(len(lista_palabras))
    word = lista_palabras.pop(0)
    guessed = []
    attempts = 6
    point = 0
    print("¡Bienvenido al Ahorcado!")
    print()
    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else: 
                progress += "_ "
        print(progress)
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            point = point + 6
            print("¡Ganaste!")
            print(f'Puntos : {point}')
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ")
        #Verifica si es mas de un caracter o si es no es alfabetico
        if len(letter) != 1 or not letter.isalpha():
            print('Entrada no valida')
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")
            print()
            point = point - 1
    else:
        point = 0
        print(f"¡Perdiste! La palabra era: {word}")
        print(f'Puntos : {point}')
    if len(lista_palabras) > 0 :
        while True :
            seleccion = input(
                'Si desea seguir jugando con la misma categoria seleccione "1"' \
                '\nSi desea salir seleccione "2" ')
            if seleccion == '1' :
                break
            elif seleccion == '2' :
                lista_palabras = []
                break
            else :
                print('Opcion invalida')
            


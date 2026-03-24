import random
words = [
        "python",
        "programa",
        "variable",
        "funcion",
        "bucle",
        "cadena",
        "entero",
        "lista",
]
word = random.choice(words)
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
    

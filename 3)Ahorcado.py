import random

def ahorcado():
    palabras = ["python", "programacion", "ahorcado", "desarrollo", "juego"]
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = []
    intentos = 6
    
    print("")
    print("¡Bienvenido al juego del Ahorcado!")
    print("_ " * len(palabra_secreta)) 
    
    while intentos > 0:
        print("")
        letra = input("Adivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta otra vez.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            print("¡Bien hecho! Esa letra está en la palabra.")
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")
            
            
        if intentos == 3:
            print("")
            print("> La palabra que se busca esta relacionada con la \"programación\"")
        elif intentos == 1:
            print("")
            print (f"> La primera letra de la palabra es \"{palabra_secreta[0]}\"")
            letras_adivinadas.append(palabra_secreta[0])   

        palabra_mostrada = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
        print(" ".join(palabra_mostrada))

        if "_" not in palabra_mostrada:
            print("")
            print("¡Felicidades! Adivinaste la palabra.")
            print("")
            break
    else:
        print("")
        print(f"Lo siento, te quedaste sin intentos. La palabra era '{palabra_secreta}'.")
        print("")

ahorcado()
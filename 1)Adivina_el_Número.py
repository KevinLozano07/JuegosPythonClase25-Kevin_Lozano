from random import randint

def adivina_el_numero():
    intentos = 0
    x = ""
    numero_secreto = randint(1, 100)
    
    print("")
    print("¡Bienvenido al juego de adivina el número!")
    print("")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")
    print("")
    
    while x == "" or x == " ":
        
        intento = int(input("Introduce tu número: "))
        intentos += 1
        distancia = (numero_secreto - intento)
        
        if intento < numero_secreto:
            print("Demasiado bajo")
            if distancia <= 10:
             print("Pero se ecunetra cerca, intente de nuevo")
            else:
             print("Y se encuentra lejos, intente de nuevo")           
        elif intento > numero_secreto:
            print("Demasiado alto")
            if distancia <= 10:
             print("Pero se ecunetra cerca, intente de nuevo")
            else:
             print("Y se ecuentra lejos, intente de nuevo")
        else:
            print("")
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            print("")
            
            x = input("¿Quiere volver a jugar? presione enter de lo contrario ingrese un valor ")
            
            if x == "" or x == " ":
             print("#" * 100)
             print("")
             print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")
             numero_secreto = randint(1, 100)
             intentos = 0
             print("")

adivina_el_numero()
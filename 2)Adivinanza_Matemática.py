import random



def adivinanza_matematica():
    operaciones = ["+", "-", "*", "/"]
    operacion = random.choice(operaciones)
    numero1 = random.randint(1, 10)
    numero2 = random.randint(1, 10)
    
    intentos = 3
    
    if operacion == "/":
        numero1 = numero1 * numero2  # Aseguramos que la división sea exacta
    
    print("")
    print("¡Bienvenido al juego de Adivinanza Matemática!")
    print("")
    
    print(f"Resuelve el siguiente problema: {numero1} {operacion} {numero2}")
    print("")
    
    while intentos > 0:
     if operacion == "+":
        respuesta_correcta = numero1 + numero2
     elif operacion == "-":
        respuesta_correcta = numero1 - numero2
     elif operacion == "*":
        respuesta_correcta = numero1 * numero2
     elif operacion == "/":
        respuesta_correcta = numero1 // numero2

     respuesta = int(input("Introduce tu respuesta: "))

     if respuesta == respuesta_correcta:
        print("")
        print("¡Correcto! Has resuelto el problema.")
        intentos = 0
        print("")
     elif intentos > 0:
         intentos -= 1
         print(f"Respuesta incorrecta te quedan {intentos} intentos")
         print("")
         if intentos == 0:
          print(f"¡Perdiste! la respuesta correcta era: {respuesta_correcta}")
          print("")

adivinanza_matematica()
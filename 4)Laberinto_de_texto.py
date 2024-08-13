def laberinto():
    laberinto = {
        "entrada": {"norte": "pasillo", "sur": None, "este": "cuarto amueblado", "oeste": None},
        "pasillo": {"norte": "salida", "sur": "entrada", "este": "cuarto oscuro", "oeste": "sala antigua"},
        "sala antigua": {"norte": "pasillo desgastado", "sur": None, "este": "pasillo", "oeste": None},
        "pasillo desgastado": {"norte": None, "sur": "sala antigua", "este": "salida", "ieste": None},
        "cuarto amueblado": {"norte": "cuarto oscuro", "sur": None, "este": None, "oeste": "entrada"},
        "puerta misteriosa": {"norte": None, "sur": None, "este": None, "oeste": "salida"},
        "cuarto oscuro": {"norte": "puerta misteriosa", "sur": "cuarto amueblado", "este": None, "oeste": "pasillo"},
        "salida": {"norte": None, "sur": "pasillo", "este": None, "oeste": None},
    }
    posicion_actual = "entrada"
    print("")
    print("¡Bienvenido al laberinto! Tienes que encontrar la salida.")

    while True:
        print("")
        direccion = input(f"Estás en {posicion_actual}. Puedes ir hacia: {list(laberinto[posicion_actual].keys())}. ¿Hacia dónde vas? ").lower()

        if direccion in laberinto[posicion_actual] and laberinto[posicion_actual][direccion]:
            posicion_actual = laberinto[posicion_actual][direccion]
            if posicion_actual == "salida":
                print("")
                print("¡Felicidades, encontraste la salida!")
                print("")
                break
        else:
            print("No puedes ir en esa dirección, intenta de nuevo.")

laberinto()
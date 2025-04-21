from src.diccionario_proyecto import datos_proyecto

# Funcion para capturar datos del template
def capturar_datos_interactivamente(datos_proyecto):
    # Itero por las claves del diccionario con las llaves y valores
    for bloque_info, datos_rellenar in datos_proyecto.items():
        # Imprimo titulo con formato del bloque
        print(f'\n---- {bloque_info.upper()} ----')
        # Itero por los valores para poder rellenar
        for dato in datos_rellenar:
            print(f'{dato.title()}:')
            datos_rellenar[dato] = input()

#if __name__ == "__main__":
#    capturar_datos_interactivamente(datos_proyecto)
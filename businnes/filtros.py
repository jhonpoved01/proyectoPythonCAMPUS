from businnes.campers import lista_campers, guardar_json

def registrar_notas_filtro():
    id_camper = int(input("Ingrese el ID del camper: "))
    
    camper_encontrado = None
    for camper in lista_campers:
        if camper.get('id') == id_camper:
            camper_encontrado = camper
            break

    if camper_encontrado:
        
        nota_teoria = float(input("Ingrese la nota teórica para el filtro: "))
        nota_practica = float(input("Ingrese la nota práctica para el filtro: "))
        notas_quices_trabajos = float(input("Ingrese la nota de quices y trabajos para el filtro: "))

        promedio_filtro = 0.3 * nota_teoria + 0.6 * nota_practica + 0.1 * notas_quices_trabajos

        notas_filtro = {
            'teorica': nota_teoria,
            'practica': nota_practica,
            'quices_trabajos': notas_quices_trabajos,
            'promedio': promedio_filtro
        }

        camper_encontrado['notas_filtro'] = notas_filtro
        if promedio_filtro >= 60:
            notas_filtro['estado_filtro'] = 'aprobado'
        else:
            notas_filtro['estado_filtro'] = 'no aprobado'
        

        print(f"Notas de filtro registradas para el camper {camper_encontrado['nombre']} {camper_encontrado['apellidos']}.")
        print(f"Nota Teórica: {nota_teoria}, Nota Práctica: {nota_practica}, Promedio: {promedio_filtro}")

        guardar_json()
    else:
        print("Camper no encontrado.")
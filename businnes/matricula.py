from businnes.campers import lista_campers, guardar_json
from businnes.aulas import lista_aulas, guardar_json_aulas

def realizar_matricula():
    
    id_camper = int(input("Ingrese el ID del camper a matricular: "))
    
    camper_matricular = None
    for camper in lista_campers:
        if camper['id'] == id_camper and camper['estado'] == 'aprobado':
            camper_matricular = camper
            break

    if not camper_matricular:
        print("Camper no encontrado o no aprobado.")
        return

    print("Rutas de entrenamiento disponibles:")
    for aula in lista_aulas:
        print(f"{aula['ruta_asignada']} - Capacidad: {aula['capacidad_actual']}/{aula['capacidad_maxima']}")

    ruta_asignada = input("Seleccione la ruta de entrenamiento para la matrícula: ")
    fecha_inicio_str = input("Ingrese la fecha de inicio (formato DD/MM/YYYY): ")
    fecha_finalizacion_str = input("Ingrese la fecha de finalización (formato DD/MM/YYYY): ")
    experto_encargado = input("Ingrese el nombre del experto encargado: ")
    salon_entrenamiento = input("Ingrese el salón de entrenamiento: ")
    trainer_encargado = input("Ingrese el nombre del trainer encargado: ")


    matricula = {
        'ruta_asignada': ruta_asignada,
        'fecha_inicio': fecha_inicio_str,
        'fecha_finalizacion': fecha_finalizacion_str,
        'experto_encargado': experto_encargado,
        'salon_entrenamiento': salon_entrenamiento,
        'trainer_encargado': trainer_encargado
    }

    camper_matricular['matricula'] = matricula
    camper_matricular['estado_matricula'] = 'matriculado'

    for aula in lista_aulas:
        if aula['ruta_asignada'] == ruta_asignada:
            aula['trainer_asignado'] = trainer_encargado

    for aula in lista_aulas:
        if aula['ruta_asignada'] == ruta_asignada:
            aula['capacidad_actual'] += 1

    guardar_json()
    guardar_json_aulas()

    print("Matrícula realizada con éxito.")
from businnes.campers import lista_campers
from businnes.trainers import lista_trainers
from businnes.aulas import lista_aulas

def listar_campers_inscritos():
    campers_inscritos = [camper for camper in lista_campers if camper.get('estado') == 'inscrito']
    if campers_inscritos:
        print("Campers en estado de inscrito:")
        for camper in campers_inscritos:
            print(camper)
    else:
        print("No hay campers en estado de inscrito.")

def listar_campers_aprobados():
    campers_aprobados = [camper for camper in lista_campers if camper.get('estado') == 'aprobado']
    if campers_aprobados:
        print("Campers que aprobaron el examen inicial:")
        for camper in campers_aprobados:
            print(camper)
    else:
        print("No hay campers que hayan aprobado el examen inicial.")

def listar_entrenadores():
    if lista_trainers:
        print("Lista de entrenadores:")
        for trainer in lista_trainers:
            print(trainer)
    else:
        print("No hay entrenadores registrados.")

def listar_campers_bajo_rendimiento():
    campers_bajo_rendimiento = [camper for camper in lista_campers if 'notas_filtro' in camper and camper["notas_filtro"].get("estado_filtro", "").lower() != "aprobado"]
    if campers_bajo_rendimiento:
        print("Campers con bajo rendimiento:")
        for camper in campers_bajo_rendimiento:
            print(camper)
    else:
        print("No hay campers con bajo rendimiento.")

def buscar_entrenador_por_ruta(ruta):
    for aula in lista_aulas:
        if aula['ruta_asignada'].lower() == ruta.lower():
            return aula['trainer_asignado']

def listar_campers_entrenador_ruta():
    ruta_asignada = input("Ingrese la ruta de entrenamiento para filtrar (java, nodejs, etc.): ")
    
    campers_entrenador_ruta = [camper for camper in lista_campers if 'matricula' in camper and camper['matricula']['ruta_asignada'].lower() == ruta_asignada.lower()]
    
    if campers_entrenador_ruta:
        print(f"Campers y entrenador asociados a la ruta {ruta_asignada}:")
        for camper in campers_entrenador_ruta:
            print(f"Camper: {camper}, Entrenador: {buscar_entrenador_por_ruta(ruta_asignada)}")
    else:
        print(f"No hay campers asociados a la ruta {ruta_asignada}.")
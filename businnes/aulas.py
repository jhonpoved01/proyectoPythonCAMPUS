from businnes.campers import lista_campers
from businnes.trainers import lista_trainers, guardar_json_trainers
import os
import json

def load_aulas_json():
    try:
        with open(os.path.join("data", "aulas.json"), 'r') as aulas_json:
            lista_aulas = json.load(aulas_json)
            print("La lista de aulas ha sido cargada")
            return lista_aulas
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")

lista_aulas = load_aulas_json()

def crear_aula():
    nombre_aula = input("Ingrese el nombre del aula: ")
    capacidad_maxima = 33
    asignar_ruta = (input("Ingrese la ruta de entrenamiento asignada al aula: ")).lower()

    aula = {
        'nombre': nombre_aula,
        'capacidad_maxima': capacidad_maxima,
        'capacidad_actual': 0,
        'ruta_asignada': asignar_ruta
    }

    lista_aulas.append(aula)
    print("Se creó el aula con éxito")
    guardar_json_aulas()

def guardar_json_aulas():
    try:
        with open(os.path.join("data", "aulas.json"), 'w') as aulas_json:
            json.dump(lista_aulas, aulas_json, indent=2)
            print("La lista de aulas ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya aulas guardadas.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")

def listar_aulas():
    print("Listado de aulas de entrenamiento: ")
    for aula in lista_aulas:
        print(aula)


def asignar_camper_a_ruta():
    id_camper = int(input("Ingrese el ID del camper: "))
    asignar_ruta = input("Seleccione la ruta de entrenamiento para el camper: ").lower()

    for camper in lista_campers:
        if camper['estado'] == 'aprobado' and camper.get('id') == id_camper:
            for aula in lista_aulas:
                if asignar_ruta == aula['ruta_asignada']:
                    if aula['capacidad_actual'] <= aula['capacidad_maxima']:
                        camper['ruta_asignada'] = asignar_ruta
                        aula['capacidad_actual'] += 1
                        guardar_json_aulas()
                        print(f"Camper asignado a la ruta {asignar_ruta}.")
                        return
                    else:
                        print(f"No hay espacio disponible en la ruta {asignar_ruta}.")
                        return

    print(f"Ruta de entrenamiento {asignar_ruta} no encontrada o camper no aprobado.")


def asignar_trainer_a_ruta():
    id_trainer = int(input("Ingrese el id del trainer para asignarle una ruta de entrenamiento: "))
    asignar_ruta_trainer = input("Ingrese la ruta de entrenamiento que impartirá el trainer: ")

    ruta_encontrada = False
    for aula in lista_aulas:
        if asignar_ruta_trainer == aula['ruta_asignada']:
            ruta_encontrada = True
            break

    if ruta_encontrada:
        for trainer in lista_trainers:
            if 'ruta_asignada' not in trainer and trainer.get('id')==id_trainer:
                trainer['ruta_asignada'] = asignar_ruta_trainer

                if 'trainers_asignados' not in aula:
                    aula['trainers_asignados'] = []

                aula['trainers_asignados'].append({
                    'nombre': trainer['Nombre'],
                    'apellidos': trainer['Apellidos']
                })

                guardar_json_aulas()
                guardar_json_trainers()
                print(f"Trainer ha sido asignado a la ruta {asignar_ruta_trainer}")
                return
            else:
                print("El trainer ya está asignado a una ruta.")
                return
    else:
        print(f"No existe la ruta {asignar_ruta_trainer}.")
import json
import os

def load_campers_json():
    try:
        with open(os.path.join("data", "campers.json"), 'r') as archivo_json:        
            lista_campers = json.load(archivo_json)
            print("La lista de campers ha sido cargada")
            return lista_campers
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")

lista_campers = load_campers_json()

def crear_camper():
    identificacion = int(input("Ingrese el número de documento: "))
    nombre = input("Ingrese el nombre del camper: ")
    apellidos = input("Ingrese los apellidos del camper: ")
    direccion = input("Ingrese la dirección del camper: ")
    acudiente = input("Ingrese el nombre del acudiente del camper: ")
    edad = int(input("Ingrese la edad del camper: "))
    email = input("Ingrese el correo electrónico del camper: ")
    telefono = input("Ingrese el número de teléfono del camper: ")
    estado = "inscrito"

    notas_prueba = {
        'teorica': 0,
        'practica': 0,
        'promedio': 0
    }

    camper = {
        'id': identificacion,
        'nombre': nombre,
        'apellidos': apellidos,
        'direccion': direccion,
        'acudiente': acudiente,
        'edad': edad,
        'email': email,
        'telefono': telefono,
        'estado': estado,
        'notas_prueba': notas_prueba
    }

    lista_campers.append(camper)
    print("Se creó el camper con éxito")
    guardar_json()

def guardar_json():
    try:
        with open(os.path.join("data", "campers.json"), 'w') as archivo_json:
            for camper in lista_campers:
                if 'notas_prueba' in camper:
                    camper['notas_prueba'] = {
                        'teorica': camper['notas_prueba']['teorica'],
                        'practica': camper['notas_prueba']['practica'],
                        'promedio': camper['notas_prueba']['promedio']
                    }
                    if 'filtro' in camper['notas_prueba']:
                        camper['filtro'] = {
                            'teorica': camper['filtro']['teorica'],
                            'practica': camper['filtro']['practica'],
                            'quices_trabajos': camper['filtro']['quices_trabajos'],
                            'promedio': camper['filtro']['promedio']
                        }
            json.dump(lista_campers, archivo_json, indent=2)
            print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")

def listar_campers():
    print("Listado de campers: ")
    for camper in lista_campers:
        print(camper)

def registrar_notas_prueba():
    id_camper = int(input("Ingrese el ID del camper: "))
    
    camper_encontrado = None
    for camper in lista_campers:
        if camper.get('id') == id_camper:
            camper_encontrado = camper
            break

    if camper_encontrado:
        
        nota_teorica = float(input("Ingrese la nota teórica: "))
        nota_practica = float(input("Ingrese la nota práctica: "))

        promedio = (nota_teorica + nota_practica) / 2

        camper_encontrado['notas_prueba'] = {'teorica': nota_teorica, 'practica': nota_practica, 'promedio': promedio}

        print(f"Notas registradas para el camper {camper_encontrado['nombre']} {camper_encontrado['apellidos']}.")
        print(f"Nota Teórica: {nota_teorica}, Nota Práctica: {nota_practica}, Promedio: {promedio}")

        if promedio >= 60:
            camper_encontrado['estado'] = 'aprobado'
            print("El camper ha sido aprobado.")
        else:
            camper_encontrado['estado'] = 'No aprobado'
            print("El camper no alcanzó la nota mínima para aprobar.")

        guardar_json()
    else:
        print("Camper no encontrado.")

def modificar_camper():
    id_camper = int(input("Ingrese el ID del camper que desea modificar: "))
    
    camper_encontrado = None
    for camper in lista_campers:
        if camper.get('id') == id_camper:
            camper_encontrado = camper
            break

    if camper_encontrado:
        print("Datos actuales del camper:")
        print(camper_encontrado)

        nombre_nuevo = input("Ingrese el nuevo nombre del camper (deje en blanco si no desea cambiar): ")
        apellidos_nuevos = input("Ingrese los nuevos apellidos del camper (deje en blanco si no desea cambiar): ")
        direccion_nueva = input("Ingrese la nueva dirección del camper (deje en blanco si no desea cambiar): ")
        acudiente_nuevo = input("Ingrese el nuevo nombre del acudiente del camper (deje en blanco si no desea cambiar): ")
        edad_nueva = input("Ingrese la nueva edad del camper (deje en blanco si no desea cambiar): ")
        email_nuevo = input("Ingrese el nuevo correo electrónico del camper (deje en blanco si no desea cambiar): ")
        telefono_nuevo = input("Ingrese el nuevo número de teléfono del camper (deje en blanco si no desea cambiar): ")

        if nombre_nuevo:
            camper_encontrado['nombre'] = nombre_nuevo
        if apellidos_nuevos:
            camper_encontrado['apellidos'] = apellidos_nuevos
        if direccion_nueva:
            camper_encontrado['direccion'] = direccion_nueva
        if acudiente_nuevo:
            camper_encontrado['acudiente'] = acudiente_nuevo
        if edad_nueva:
            camper_encontrado['edad'] = int(edad_nueva)
        if email_nuevo:
            camper_encontrado['email'] = email_nuevo
        if telefono_nuevo:
            camper_encontrado['telefono'] = telefono_nuevo

        print("Datos modificados con éxito.")
        guardar_json()
    else:
        print("Camper no encontrado.")
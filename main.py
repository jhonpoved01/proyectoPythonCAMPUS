from commons.menus import *
from commons.utlis import*
from blockbuster.actores import *
def load_actores_json():
    limpiar_pantalla()
    op=menu_principal()
    if op==1:
       Administracion_de_generos()
       input("Presiona cualquier tecla para continuar: ")
    if op==2:
       Administracion_de_actores()
       input("Presiona cualquier tecla para continuar: ")
    if op==3:
       Administracion_de_formatos()
       input("Presiona cualquier tecla para continuar: ")
    if op==4:
        gestor_de_informes()
        input("Presiona cualquier tecla para continuar: ")
    if op==5:
        gestor_de_peliculas()
        input("Presiona cualquier tecla para continuar: ")


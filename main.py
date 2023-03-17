"""Proyecto Modulo 1 de Programación III..."""

#from proyecto.ui.ui import *

#from proyecto.ui import ui
from ui import ui
from api import api

def main():
    """Orden y llamado de los modulos y sus funciones..."""
    print("----------------------Bienvenido----------------------\n")
    print("Esta API ha sido suministrada por el portal Nacional de Datos Abiertos...")
    print("A continuación, realice su consulta\n")
    depto = ui.nombre_departamento()
    lim = ui.limite_registros()
    
    print("")
    resultado = api.consulta_base(depto, lim)
    ui.visualizar(resultado)
    
main()
ui.esperar()

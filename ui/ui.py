"""UI del programa"""

def nombre_departamento():
    """almacena la string con la que se ejecutará la solicitud"""
    depto = input ("Departamento al que desea consultar: ")
    return format(depto.upper())

def limite_registros():
    """establecerá un límite para evitar que el programa se 'cuelgue'"""
    lim = input ("¿Cuántos registros quiere obtener? (No superior a 1000)")
    return int (lim)

def visualizar(resultado):
    """recibirá los datos de otro modulo para finalmente mostrarlos en la consola"""
    print (resultado)
    
def esperar():
    """Evita que se cierre la terminal al terminar de mostrar la consulta"""
    input("Enter para cerrar...")

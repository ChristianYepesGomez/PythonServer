from configparser import ConfigParser


def config(archivo='connection.ini', seccion='postgresql'):
    # Parsear el archivo
    parser = ConfigParser()
    parser.read(archivo)

    # Ir a la sección de postgresql y extraer los parámetros
    db = {}
    if parser.has_section(seccion):
        params = parser.items(seccion)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Secccion {0} no encontrada en el archivo {1}'.format(seccion, archivo))

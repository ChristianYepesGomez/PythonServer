import pgdb
from db.config import config


class AerdataPipeline(object):

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        conexion = None
        try:
            # Lectura de los parámetros de conexion
            params = config()

            # Conexion al servidor de PostgreSQL
            print('Conectando a la base de datos PostgreSQL...')
            conexion = pgdb.connect(**params)

            # creación del cursor
            cur = conexion.cursor()

            # Ejecución la consulta para obtener la conexión
            print('La version de PostgreSQL es la:')
            cur.execute('SELECT version()')

            # Se obtienen los resultados
            db_version = cur.fetchone()
            # Se muestra la versión por pantalla
            print(db_version)

            # Cerremos el cursor
            cur.close()
        except Exception as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()
                print('Conexión finalizada.')

    def process_item(self, item, spider):
        print(item["name"])

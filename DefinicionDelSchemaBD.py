import mysql.connector
from mysql.connector import errorcode

try:
    # Conexión al servidor de MySQL
    conexion = mysql.connector.connect(
        user='root',
        password='12345',
        host='localhost'
    )

    if conexion.is_connected():
        print("Conexión exitosa al servidor de MySQL")
        
        # Crear cursor para ejecutar comandos SQL
        cursor = conexion.cursor()

        # Leer el contenido del archivo SQL
        with open(r"sql\DDL.sql", 'r') as file:
            script_sql = file.read()

        # Separar el script en comandos individuales
        comandos_sql = script_sql.split(';')

        # Ejecutar cada comando SQL por separado
        for comando in comandos_sql:
            if comando.strip():
                cursor.execute(comando)

        # Commit para asegurar que los cambios se apliquen
        conexion.commit()

        print("Script ejecutado exitosamente")

        # Cerrar cursor y conexión
        cursor.close()
        conexion.close()
        print("Conexión cerrada")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error de acceso: Usuario o contraseña incorrectos")
    else:
        print("Error de MySQL:", err)

except FileNotFoundError:
    print("Error: No se encontró el archivo SQL")

except ImportError:
    print("Error: mysql.connector no está instalado")

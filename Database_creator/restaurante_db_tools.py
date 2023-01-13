import sqlite3


# Creamos la base de datos
def crear_bd():
    link = sqlite3.connect('restaurante.db')
    print("Successfully Connected to SQLite")
    cursor = link.cursor()

    try:
        cursor.execute('''
            CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL
            );
        ''')

        cursor.execute('''
            CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id)
            );
        ''')

    except sqlite3.OperationalError as Error:
        print("Error: ", Error)

    else:
        print("La tabla Categorias y Platos se han creado correctamente")

    
    finally:
        if link:
            link.close()
            print("The SQLite connection is closed")


# Agregamos elementos a la tabla categoria
def agregar_categoria():
    nueva_categoria = input('Ingresa el nombre de la categoria a agregar: ')

    link = sqlite3.connect('restaurante.db')
    print('Successfully Connected to SQLite')

    cursor = link.cursor()
 
    try:
        cursor.execute(f"INSERT INTO categoria (nombre) VALUES('{nueva_categoria}')") 
        link.commit()
    
    except sqlite3.IntegrityError:
        print(f"La categoria {nueva_categoria} ya existe")

    finally:
        if link:
            link.close()
            print("The SQLite connection is closed")

# Agregamos elementos a la tabla plato

def agregar_plato():
    link = sqlite3.connect('restaurante.db')
    cursor = link.cursor()

    cursor.execute('SELECT * FROM categoria')
    categorias = cursor.fetchall()

    print('Categorias disponibles')
    for categoria in categorias:
        print(f"[{categoria[0]}] {categoria[1]}")

    try:
        categoria_usuario = int(input('\nElige la categoria deseada: '))
    except ValueError:
        print("Error: Debes ingresar el numero de la categoria")
        return

    cursor.execute("SELECT MAX(id) FROM categoria")
    maximo = cursor.fetchone()[0]

    if categoria_usuario < 1 or categoria_usuario > maximo:
        print("Categoria invalida")
        return

    plato = input('Ingresa el nombre del nuevo plato: ')

    try:
        cursor.execute(f"INSERT INTO plato(nombre, categoria_id) VALUES ('{plato}', {categoria_usuario})")
        link.commit()

    except sqlite3.IntegrityError:
        print(f"El plato {plato} ya existe")

    finally:
        if link:
            link.close()
            print("The SQLite connection is closed")

# Mostramos el menu

def mostrar_menu():
    link = sqlite3.connect('restaurante.db')
    print("Successfully Connected to SQLite\n\n")

    cursor = link.cursor()

    categorias = cursor.execute('SELECT * FROM categoria').fetchall()

    for categoria in categorias:
        print(categoria[1])

        platos = cursor.execute(f"SELECT * FROM plato WHERE categoria_id = {categoria[0]}").fetchall()
        for plato in platos:
            print(f"\t{plato[1]}")
    
    link.close()
from setuptools import setup

setup(
    name = 'Database_creator',
    version= '1.0',
    description= 'Un paquete para crear una base de datos sencilla en SQLite para un restaurante',
    author= 'Jose Armando Rosas Balderas',
    author_email= 'armando.rosas133@gmail.com',
    url= 'https://github.com/ArmandoRosasB',
    packages= ['Database_creator', 'Database_creator.restaurante_db_tools'],
    scripts= ['restaurante.py']
)
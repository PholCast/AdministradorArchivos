import os
import zipfile


def unzip(zip_file_path):
    # Path to the .zip file


    # Directorio de destino donde se extraerá el contenido (la carpeta madre)
    #le puse
    destination_directory = 'no me voy a doxear'

    """ Verifica si la carpeta madre existe, y si no se crea:
    if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)"""

    # Descomprime el archivo .zip en la carpeta madre
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_directory)

    listItems= os.listdir(destination_directory)

    for item in listItems:
        item_path = os.path.join(destination_directory, item)
        if os.path.isdir(item_path):
            return item_path


    
    return destination_directory


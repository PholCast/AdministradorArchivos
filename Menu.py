from Tree import GeneralTree
from Manager import Manager
class Menu:
    @staticmethod
    def MainOptions():
        while(True):
            print("\n")
            option = int(input("1.Buscar\n2.Crear\n3.Eliminar\n4.Finalizar Programa\n¿Que deseas hacer?: "))
            if 0 < option <=4 :
                break
            else:
                print("Opcion invalida")
        
        match option:
            case 1:
                Manager.search()
            case 2:
                Menu.addOptions()
                #Manager.add()
            case 3:
                Manager.delete()
            case 4:
                return False
    @staticmethod
    def addOptions():
        while(True):
            print("\n")
            addOption = int(input("1.Agregar Archivo\n2.Agregar Carpeta\n3.Salir\n¿Que deseas hacer?: "))
            if 0 < addOption <=3 :
                break
            else:
                print("Opcion invalida")
        
        match addOption:
            case 1:
                Manager.addFile()
            case 2:
                Manager.addFolder()
            case 3:
                return
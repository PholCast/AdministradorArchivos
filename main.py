from Tree import GeneralTree
from Manager import Manager
from Menu import Menu
def main():
    inputZip = input("Ingresa la ruta del zip: ")
    Manager.treeManager = GeneralTree(inputZip)

    while(True):
        if(Menu.MainOptions()==False):
            break
    
    print("¡Programa finalizado con exito!\n")
    
    #print(Manager.treeManager.root)
    #print(Manager.treeManager.root.path)
    #newTree = GeneralTree(inputZip)
    #print(f"Esta es la raiz:{newTree.root}")
    #newTree.traverse(newTree.root)
    Manager.treeManager.print_tree()
main()


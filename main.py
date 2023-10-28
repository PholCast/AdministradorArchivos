from Tree import GeneralTree
def main():
    inputZip = input("Ingresa la ruta del zip")

    newTree = GeneralTree(inputZip)
    print(f"Esta es la raiz:{newTree.root}")

    newTree.traverse(newTree.root)
main()


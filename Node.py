#We could add more attributes

class Node:
    def __init__(self,name,path,typeElement,elementSize,CreationDate,isFolder):
        self.name = name
        self.path = path
        self.typeElement = typeElement
        self.elementSize = elementSize #peso
        self.CreationDate = CreationDate
        self.children = []
        self.isFolder = isFolder
    
    def __repr__(self):
        return self.name+": "+ self.typeElement
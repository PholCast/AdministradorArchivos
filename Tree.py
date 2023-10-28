import os
from UsingZipOs import unzip
from datetime import datetime
from Node import Node

class GeneralTree:
    def __init__(self, zipPathfile):

        self.root = unzip(zipPathfile)
        self.root = self.buildTree(self.root)

 
    def traverse(self, current):
        if(current is not None):
            print(current)
            for child in current.children:
                self.traverse(child)


    def buildTree(self,folderPath):
        node = self.createNodeFromPath(folderPath)

        for item in os.listdir(folderPath):
            item_path = os.path.join(folderPath, item)
            print("item_path es:",item_path)
            is_directory = os.path.isdir(item_path)

            if is_directory:
                newNode = self.buildTree(item_path)
            else:
                newNode = self.createNodeFromPath(item_path)
            
            node.children.append(newNode)
        
        return node
    

    def createNodeFromPath(self,path):
        #Get just the name 
        name = os.path.basename(path)

        isFolder = os.path.isdir(path)


        if isFolder:
            typeElement = "Folder"
        else:
            #Extension such as pptx, .txt, .xlsx and so on
            typeElement = os.path.splitext(name)[1]


        elementSize = os.path.getsize(path)

        creationTime = os.path.getctime(path)
        creation_datetime = datetime.fromtimestamp(creationTime)
        creationDate = creation_datetime.strftime('%Y-%m-%d %H:%M:%S')

        return Node(name,path,typeElement,elementSize,creationDate,isFolder)
import json
import sys
import glob
import os
import tempfile
from datetime import date
from functools import wraps
from pathlib import Path
from reporter.header import create_header
from reporter.graph import graph
import matplotlib

matplotlib.use('Agg')

class ReporterGenerator:
    '''
    The main objective is to build a file markdown.md in the /data directory 
    '''
    path_file_author = ""
    path_file_excell = ""
    path_file_picture = ""
    path_file_markdown = ""
    markdown = ""
    header = ""
    image_path = ""

    def __init__(self, pathvar):
        path1 = Path(pathvar)
        if not path1.is_dir:
            print('Error path')
        else:
            mypath = f'Path is {path1}'
            print(mypath)
        # create all usefull path 
        self.path_file_author = (path1/'authors.json')
        self.path_file_picture = (path1/'graph.png')
        self.path_file_markdown = (path1/'markdown.md')
        # check validity 
        if not self.path_file_author.is_file:
            print('Error author file')
        else:
            mypath = f'Author file is OK : {path1}'
            print(mypath)   

        # search excell file in directory ( get the first one )  
        listfile = list(Path(pathvar).glob('*.xlsx'))  
        mypath = f'Excell file is  : {listfile[0]}'      
        self.path_file_excell = (listfile[0])
        print(self.path_file_excell)

    def methode0(self):   # c'est une méthode de la classe avec lme slef
        print("Methode0")

    def methode1(self):
        print("Methode1")

    def addheader(self):
        place = 'Marseille'
        print(str(self.path_file_author))
        self.header = create_header(str(self.path_file_author), place) 

    def addplot(self):
        # call the plot api ( pass the path to excell - retrieve picture file path )
        # self.path_file_plot = call( path_file_excell )
        fichier=tempfile.mktemp("graph2.png")
        graph(file=str(self.path_file_excell),output_file=str(self.path_file_picture))

    def build_result(self):
        self.markdown  = self.header    
        addImg = f'<img src="{self.path_file_picture}">'   
        self.markdown += addImg
        print("Done !")
        print(self.markdown)
        new_file = open(str(self.path_file_markdown),'w')
        new_file.write(self.markdown)
        new_file.close()

'''
init ( path fichiuer dir fichier json / excell )=> constructeur passer dossier 
authors.json à lister 
prendre fichier excell fini par xls 

addheader
addplot / module grapher sauver en image

gene = ReporterGenerator('/home/eric/reporter')
gene.addheader()
gene.plot_image() => call module externe
gene.poeme()
gene.buildResult() 

'''

if __name__ == "__main__":
    module_dir = os.path.abspath(os.path.dirname(__file__))
    module_dir = Path(module_dir)/'../data'
    print(str(module_dir))
    gene = ReporterGenerator(module_dir)
    gene.addheader()
    gene.addplot()
    gene.build_result()

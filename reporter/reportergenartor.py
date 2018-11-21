import json
import sys
import glob
import os
from datetime import date
from functools import wraps
from pathlib import Path
from reporter.header import create_header


class ReporterGenerator:
    path_file_author = ""
    path_file_excell = ""
    path_file_plot = ""
    markdown = ""
    header = ""
    image_path = ""

    def __init__(self, pathvar):
        path1 = Path(pathvar)
        #module_dir = os.path.abspath(os.path.dirname(__file__))
        if not path1.is_dir:
            print('Error path')
        else:
            mypath = f'Path is {path1}'
            print(mypath)
        # create all usefull path 
        self.path_file_author = path1/'authors.json'
        # check validity 
        if not self.path_file_author.is_file:
            print('Error author file')
        else:
            mypath = f'Author file is OK : {path1}'
            print(mypath)   

        # search excell file in directory ( get the first one )  
        listfile = list(Path(pathvar).glob('*.xlsx'))  
        mypath = f'Excell file is  : {listfile[0]}'      
        self.path_file_excell = listfile[0]
        print(self.path_file_excell)

    def methode0(self):   # c'est une méthode de la classe avec lme slef
        print("Methode0")

    def methode1(self):
        print("Methode1")

    def addheader(self):
        place = 'Marseille'
        self.header = create_header(self.path_file_author, place) 

    def addplot(self):
        # call the plot api ( pass the path to excell - retrieve picture file path )
        # self.path_file_plot = call( path_file_excell )
        self.path_file_plot = ""

    def build_result(self):
        self.markdown  = self.header    
        addImg = f'<img src="{self.image_path}">'   
        self.markdown += addImg
        print("Done !")

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
gene = ReporterGenerator('/Users/eric/report')
gene.addheader()
gene.addplot()
gene.build_result()


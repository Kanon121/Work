
#Script created by Kanon
#This script will replace all files in a folder with a zip of its contents excluding .py, .swp, and .zip



import os
from os import listdir
from os.path import isfile, join
import zipfile
from zipfile import ZIP_DEFLATED

class RarFiles():
    def __init__(self, path):
        self.files = []
        self.currdir = path
        self.GetFiles(path)
        self.CreateZips(path)
    def GetFiles(self, path):
        for f in os.listdir(path):
            self.files.append(f)
    def CreateZips(self, path):
        for f in self.files:
			print f			
			if f.endswith('.bak'):
				zipp = zipfile.ZipFile((path + '/' + f + '.zip'), 
					'w', zipfile.ZIP_DEFLATED)
				print f
				zipp.write(f, f)
				zipp.close()
				os.remove(path + '/' + f)
		        
rar = RarFiles('/home/kanon/Desktop/rar/')
                        

#Example: 
#rar = RarFiles("/home/kanon/Desktop/rar")

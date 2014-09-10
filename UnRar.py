import shutil
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
			if f.endswith('.zip'):
				self.files.append(f)

	def CreateZips(self, path):
		for f in self.files:
			zipp = zipfile.ZipFile((path + '/' + f), 
				'r', zipfile.ZIP_DEFLATED)
			cut = len(f)
			cut -= 4		
			zipp.extractall(path)
			zipp.close()

PATH = '/home/kanon/Desktop/rar/'					        
rar = RarFiles(PATH)

class MoveFiles():
	def __init__(self):
		self.files = []
		for f in os.listdir(PATH):
			if f.endswith('.zip'):
				self.files.append(f)
		for f in self.files:
			cut = len(f)
			cut -= 4
			print f
			newPath = PATH + 'home/kanon/Desktop/rar/'
			
			shutil.copy(newPath + f[0:cut], PATH)
			os.remove(PATH + f)


copy = MoveFiles()

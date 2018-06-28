import os
import cv2
import numpy as np
from scipy import ndimage
import scipy.misc

PATH = os.path.join('/media','SSD1','MFISH_Dataset','MFISH_original')
PATH_save = os.path.join('/media','SSD1','MFISH_Dataset','MFISH_max')

folders = os.listdir(PATH)
folders.remove('README.TXT')
print(folders)
for f in folders:
	folders_in = os.listdir(os.path.join(PATH,f))
	ID_main = f[0:3]
	images = []
	chain = []
	try:
		os.mkdir(os.path.join(PATH_save,f))
	except:
		print(os.path.join(PATH_save,f),'already exists')
	for im_name in folders_in:
		ID = im_name[3:5]
		if im_name != 'Case Info':
			# search for the ID in the list
			if ID not in images:
				images.append(ID)
				chain.append([ID+'/'+os.path.join(PATH,f,im_name)])
			else:
				chain[images.index(ID)].append(ID+'/'+os.path.join(PATH,f,im_name))
	for i in range(len(chain)):
		for idx, path in enumerate(chain[i]):
			if 'K' in path:
				scipy.misc.imsave(os.path.join(PATH_save,f,ID_main+path[0:2]+'K.png'),ndimage.imread(path[3:]))
			else:
				if idx == 0:
					im = np.asarray(ndimage.imread(path[3:]))
				else:
					im = np.amax([np.asarray(ndimage.imread(path[3:])), im], axis = 0)
		scipy.misc.imsave(os.path.join(PATH_save,f,ID_main+path[0:2]+'m.png'), im)
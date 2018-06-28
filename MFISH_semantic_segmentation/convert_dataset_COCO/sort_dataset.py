import os
import numpy as np
from scipy import ndimage
import scipy.misc

# -------------------------------------------------------------------- #
#                            Parameters                                #
# -------------------------------------------------------------------- #

PATH = os.path.join('/media','SSD1','MFISH_Dataset','MFISH_original')    # path to the original dataset
PATH_temp = os.path.join('/media','SSD1','MFISH_Dataset','MFISH_max')    # temporal dataset 
PATH_SORT = os.path.join('/media','SSD1','MFISH_Dataset','MFISH_split')  # folder which will contain the processed dataset

train_partition = 50
test_partition = 25
val_partition = 25

remove_temp = False

# -------------------------------------------------------------------- #
#                                end                                   #
# -------------------------------------------------------------------- #

folders = os.listdir(PATH)
folders.remove('README.TXT')
print(folders)
for f in folders:
	folders_in = os.listdir(os.path.join(PATH,f))
	ID_main = f[0:3]
	images = []
	chain = []
	try:
		os.mkdir(os.path.join(PATH_temp,f))
	except:
		print(os.path.join(PATH_temp,f),'already exists')
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
				scipy.misc.imsave(os.path.join(PATH_temp,f,ID_main+path[0:2]+'K.png'),ndimage.imread(path[3:]))
			else:
				if idx == 0:
					im = np.asarray(ndimage.imread(path[3:]))
				else:
					im = np.amax([np.asarray(ndimage.imread(path[3:])), im], axis = 0)
		scipy.misc.imsave(os.path.join(PATH_temp,f,ID_main+path[0:2]+'m.png'), im)



folders = os.listdir(PATH_temp)


class db():
	def __init__(self,PATH_in,PATH_out,train_p=50,val_p=25,test_p=25):
		self.number = []
		for f in folders:
			folders_in = os.listdir(os.path.join(PATH_in,f))
			ID_main = f[0:3]
			images = []
			chain = []
			for im_name in folders_in:
				ID = im_name[3:5]
				if ID not in images:
					images.append(ID)
			self.number.append([len(images),f])

		self.PATH_in = PATH_in
		self.PATH_out = PATH_out
		self.len = 0
		self.number.sort()
		self.number.reverse()
		self.train = {'len':0,'dir':[]}
		self.val = {'len':0,'dir':[]}
		self.test = {'len':0,'dir':[]}
		for j in self.number:
			if self.train['len']/train_p <= self.val['len']/val_p and self.train['len']/train_p < self.test['len']/test_p:
				self.train['len'] += j[0]
				self.train['dir'].append(j[1])
			elif self.test['len']/test_p <= self.train['len']/train_p and self.test['len']/test_p <= self.val['len']/val_p:
				self.test['len'] += j[0]
				self.test['dir'].append(j[1])
			elif self.val['len']/val_p < self.test['len']/test_p and self.val['len']/val_p < self.train['len']/train_p:
				self.val['len'] += j[0]
				self.val['dir'].append(j[1])
			else:
				print('Train:',self.train['len'],'. Val:', self.val['len'], '. Test:', self.test['len'])

			self.len += j[0]
		
	def __len__(self):
		return self.len
	def mkdatabase(self):
		for folder in [[self.train,'train'], [self.val,'val'], [self.test,'test']]:
			for j in folder[0]['dir']:
				annotations = 'cp -r '+os.path.join(self.PATH_in,j,'*K.png')+' '+os.path.join(self.PATH_out,folder[1],'annotations')
				x2018 = 'cp -r '+os.path.join(self.PATH_in,j,'*m.png')+' '+os.path.join(self.PATH_out,folder[1],folder[1]+'2018')
				os.system(annotations)
				os.system(x2018)
	def ch_name(self):
		for folder in ['train','test','val']:
			list_im_annotation = os.listdir(os.path.join(self.PATH_out,folder,'annotations'))
			for i in list_im_annotation:
				string = 'mv '+os.path.join(self.PATH_out,folder,'annotations',i)+' '+os.path.join(self.PATH_out,folder,'annotations',i[0:5]+'.png')
				os.system(string)
			list_im_real = os.listdir(os.path.join(self.PATH_out,folder,folder+'2018'))
			for i in list_im_real:
				string = 'mv '+os.path.join(self.PATH_out,folder,folder+'2018',i)+' '+os.path.join(self.PATH_out,folder,folder+'2018',i[0:5]+'.png')
				os.system(string)

if remove_temp:
	os.system('rm -r '+PATH_temp)


cariotipo = db(PATH_MAX,PATH_SORT,train_partition,val_partition,test_partition)
cariotipo.mkdatabase()
cariotipo.ch_name()

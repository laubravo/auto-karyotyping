import os
import numpy as np
from scipy import ndimage
import scipy.misc as misc

# -------------------------------------------------------------------- #
#                            Parameters                                #
# -------------------------------------------------------------------- #

PATH = os.path.join('/mnt/tmp/home4/gjeanneret/SSD/MFISH_Dataset','MFISH_original')    # path to the original dataset
NAME_OUT = 'MFISH_split'
PATH_SORT = '/mnt/tmp/home4/gjeanneret/SSD/MFISH_Dataset'  # folder which will contain the processed dataset

train_partition = 50
test_partition = 25
val_partition = 25

# This functions is should return an image given a list containing 2 pictures ([picture1, picture2])

def best(im_vec):
    if np.std(im_vec[0],keepdims=False)>np.std(im_vec[1],keepdims=False):
        return im_vec[0]
    else:
        return im_vec[1]

def max_im(im_vec):
    return np.amax(im_vec, axis = 0)


# -------------------------------------------------------------------- #
#                                end                                   #
# -------------------------------------------------------------------- #

PATH_SORT = os.path.join(PATH_SORT, NAME_OUT)

if not os.path.exists(os.path.join(PATH_SORT)):
    os.mkdir(os.path.join(PATH_SORT))
    os.mkdir(os.path.join(PATH_SORT,'train'))
    os.mkdir(os.path.join(PATH_SORT,'train','annotations'))
    os.mkdir(os.path.join(PATH_SORT,'train','train2018'))
    os.mkdir(os.path.join(PATH_SORT,'val'))
    os.mkdir(os.path.join(PATH_SORT,'val','annotations'))
    os.mkdir(os.path.join(PATH_SORT,'val','val2018'))
    os.mkdir(os.path.join(PATH_SORT,'test'))
    os.mkdir(os.path.join(PATH_SORT,'test','annotations'))
    os.mkdir(os.path.join(PATH_SORT,'test','test2018'))


class db():
    def __init__(self,PATH_in,PATH_out,train_p=50,val_p=25,test_p=25):
        folders = os.listdir(PATH)
        folders.remove('README.TXT')
        temp = []
        self.main_list = []
        for folder in folders:
            folders_in = os.listdir(os.path.join(PATH_in,folder))
            ID_main = folder[0:3]
            #temp.append(folder[0:3])
            images_ID = []
            chain = []
            # take the images within the folder
            #print(folder)
            path_to_main = os.listdir(os.path.join(PATH_in,folder))
            path_to_main.sort()
            try:
                if path_to_main.index('Case Info')!=999999:
                    path_to_main.remove('Case Info')
            except ValueError:
                print(path_to_main)
            
            self.main_list.append([len(path_to_main),folder,path_to_main])
        self.main_list.sort()
        self.PATH_in = PATH_in
        self.PATH_out = PATH_out
        self.train = {'len':0}
        self.val = {'len':0}
        self.test = {'len':0}
        self.max_path = []
        self.train_p = train_p
        self.test_p = test_p
        self.val_p = val_p
    def sort(self,function):
        for n,folder,main in self.main_list:
            # get the partition per folder
            IDs = []
            tupla = [] # [label(ID+ID_temp+.png),max,ground_truth]
            for image in main:
                ID_temp = image[0:7]
                im = ndimage.imread(os.path.join(self.PATH_in, folder, image))
                if ID_temp not in IDs:
                    IDs.append(ID_temp)
                    tupla.append([ID_temp,np.zeros(im.shape),np.zeros(im.shape)])
                    if 'K.png' in image:
                        tupla[-1][2] = im
                    else:
                        tupla[-1][1] = im
                else:
                    idx = IDs.index(ID_temp)
                    if 'K.png' in image:
                        tupla[idx][2] = im
                    else:
                        # -----------------------------------#
                        #    here it is done the operation   #
                        # -----------------------------------#
                        tupla[idx][1] = function( [tupla[idx][1],im])
            # adds to train, val or test every image
            if self.train['len']/self.train_p <= self.val['len']/self.val_p and self.train['len']/self.train_p < self.test['len']/self.test_p:
                # saves image and anotation
                self.train['len'] += save_tuple(tupla,'train',self.PATH_out)
                
            elif self.test['len']/self.test_p <= self.train['len']/self.train_p and self.test['len']/self.test_p <= self.val['len']/self.val_p:
                # saves image and anotation
                self.test['len'] += save_tuple(tupla,'test',self.PATH_out)
                
            elif self.val['len']/self.val_p < self.test['len']/self.test_p and self.val['len']/self.val_p < self.train['len']/self.train_p:
                # saves image and anotation
                self.val['len'] += save_tuple(tupla,'val',self.PATH_out)
                

def save_tuple(tupla,folder,PATH_out):
    # check if there's no K's
    cont = 0
    for ID, image, ground_truth in tupla:
        #print(type(ID))
        #print(type(image))
        #print(type(PATH_out))
        if np.sum(ground_truth)!=0:
            name = ID+'.png'
            fullfile_im = os.path.join(PATH_out,folder,folder+'2018',name)
            fullfile_gt = os.path.join(PATH_out,folder,'annotations',name)
            misc.imsave(fullfile_im,image)
            misc.imsave(fullfile_gt,ground_truth)
            cont += 1
    return cont




cariotipo = db(PATH,PATH_SORT,train_partition,val_partition,test_partition)
cariotipo.sort(best)
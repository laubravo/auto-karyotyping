import random
import os
import sys
from shutil import copyfile
import pdb

# Function definitions

# create set folder with cromosomes subfolders
def create_set(base_path, set_name):
	chromosome_num = 23
	set_path = os.path.join(base_path, set_name)
	os.makedirs(set_path)
	# create all cromosome (class) subfolders
	for chrom in range(1,chromosome_num+1):
		os.makedirs(os.path.join(set_path, str(chrom)))

# copy each image from old database into appropriate cromosome folder in set
def get_chromosomes_in_folder(base_path, save_path):
	
	# get file names inside cromosome directory
	full_path = os.path.join(base_path)
	file_names = os.listdir(full_path)
	# get cromosome number of file 
	file_chromosome_folder = [int(i.split(' ')[1][:-5]) for i in file_names]
	# copy file and store in set (save_path) cromosome folder
	#pdb.set_trace()
	for f in range(0,len(file_names)):
		source_path = os.path.join(base_path,file_names[f])
		dst_path = os.path.join(save_path,str(file_chromosome_folder[f]),file_names[f])
		copyfile(source_path, dst_path)


######################################################

# generate random selection of cariotypes for DB sets
num_cariotypes = 119
num_train = 80
num_val = 19

order = random.sample(range(1,num_cariotypes+1),num_cariotypes)

OLD_DATABASE_PATH = './single_chromosomes'
NEW_DATABASE_PATH = './classificationDB'
set_names = ['Train','Val','Test']

for current_set in set_names:
    # create database and set subfolders
    if not os.path.exists(os.path.join(NEW_DATABASE_PATH,current_set)):
        create_set(NEW_DATABASE_PATH, current_set)
    # copy image files to correct set folder
    if current_set == 'Train':
    	cariotype_folders = order[0:num_train]
    if current_set == 'Val':
    	cariotype_folders = order[num_train:(num_train+num_val)]
    if current_set == 'Test':
    	cariotype_folders = order[(num_train+num_val):]
    
    for folder_num in cariotype_folders:
    	BASE_PATH = os.path.join(OLD_DATABASE_PATH, str(folder_num))
    	SAVE_PATH = os.path.join(NEW_DATABASE_PATH, current_set)
    	get_chromosomes_in_folder(BASE_PATH, SAVE_PATH)




 




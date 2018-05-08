import numpy as np
import nibabel as nib
import scipy.io
from os.path import join as pjoin, split as psplit
import os
import json
import numpy as np
from skimage import measure
from pprint import pprint
import operator
from sklearn.metrics import precision_recall_fscore_support


data = json.load(open('bbox_coco_2014_minival_resultsLast.json'))

y_trueB = []
for i in range (len(data)):
#     if ((data[i]['image_id'] == data[i-1]['image_id']) & (data[i]['score'] > data[i-1]['score'])):
#         y_true.remove(y_true[i-1])    
#         y_true.append([data[i]['image_id'], data[i]['category_id'], data[i]['score']])
#     else:
    y_trueB.append([data[i]['image_id'], data[i]['category_id'], data[i]['score']])
#         y_true.append(data[i]['image_id'])
                    
        
y_true = []
cat = []
y_trueB = sorted(sorted(y_trueB, key=operator.itemgetter(2), reverse=True), key=operator.itemgetter(0))
for i in range (len(y_trueB)):
    if ((y_trueB[i][0] == y_trueB[i-1][0]) & (y_trueB[i][2] < y_trueB[i-1][2])):
        print 'hola'
#         y_true.remove(y_true[i-1])    
#         y_true.append([data[i]['image_id'], data[i]['category_id'], data[i]['score']])
    else:
        y_true.append([y_trueB[i][0], y_trueB[i][1], y_trueB[i][2]])
        cat.append(y_trueB[i][1])
#         y_true.append(data[i]['image_id'])
                    
        
data = json.load(open('instances_minival2014.json'))

y_trueR = []
for i in range (len(data['annotations'])):
#     if ((data[i]['image_id'] == data[i-1]['image_id']) & (data[i]['score'] > data[i-1]['score'])):
#         y_true.remove(y_true[i-1])    
#         y_true.append([data[i]['image_id'], data[i]['category_id'], data[i]['score']])
#     else:
    y_trueR.append(data['annotations'][i]['category_id'])
#         y_true.append(data[i]['image_id'])
                    
        


y_true = y_trueR
y_pred = cat
pos_label = y_true
x = precision_recall_fscore_support(y_true, y_pred, average=None)
AP = np.mean(x[2])
         
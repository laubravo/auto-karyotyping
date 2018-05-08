import numpy as np
import nibabel as nib
import scipy.io
from os.path import join as pjoin, split as psplit
import os

from pycocotools import mask
from PIL import Image, ImagePalette # For indexed images
# import matplotlib # For Matlab's color maps

import json
from skimage import measure

import cv2
from matplotlib import pyplot as plt
import matplotlib.patches as patches

from scipy import ndimage as ndi
from skimage.morphology import disk, closing
from skimage.segmentation import clear_border, join_segmentations
from skimage.filters import rank, threshold_otsu
import io
import pdb


in_dir = '/media/user_home1/lcastillo/biologia/classificationDB/Train/'
out_dir = '/media/user_home1/lcastillo/biologia/Train2014/'
# i = '1'
# temp_name = '2 1a.bmp'
info_im = []

if not os.path.exists(out_dir):
        os.makedirs(out_dir)
               
# def create(j):
#     temp_name = image_list[j]        
#     info = [index,temp_name]
#     info_im.append(info)

#     img = Image.open(in_dir + i +'/'+temp_name)
#     img = np.array(img)
#     img.save(out_dir + 'COCO_train2015_'+index+'.jpg', 'jpeg')
#     tophat = ndi.white_tophat(img,5)
#     otsu = threshold_otsu(tophat)
#     mask = (img>otsu).astype(np.uint8)
#     im2,contours,hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     cnt = contours[0]
#     M = cv2.moments(cnt)

#     x,y,w,h = cv2.boundingRect(cnt)
#     segmentation = []
#     area = cv2.contourArea(contours[0])

#     for contour in contours:
#         contour = contour.flatten().tolist()
#         segmentation.append(contour)
     
#     # images_info.append( 
#     #     {
#     #         "license": 1,
#     #         "file_name": 'COCO_train2015_'+index+'.jpg',
#     #         "coco_url": "",
#     #         "height": img.shape[0],
#     #         "width": img.shape[1],
#     #         "date_captured": "ni idea",
#     #         "flickr_url": "",
#     #         "id": index
#     #     },
#     # )

#     # labels_info.append(
#     #     {
#     #         "segmentation": segmentation,  # poly
#     #         "area": area,  # segmentation area
#     #         "iscrowd": 0,
#     #         "image_id": index,
#     #         "bbox": [x, y, w, h],
#     #         "category_id": i,
#     #         "id": index + 500
#     #     },
#     # )

#       images_info={
#         "license": 1,
#         "file_name": 'COCO_train2015_'+index+'.jpg',
#         "coco_url": "",
#         "height": img.shape[0],
#         "width": img.shape[1],
#         "date_captured": "ni idea",
#         "flickr_url": "",
#         "id": index
#         },

#     labels_info = 
#         {
#             "segmentation": segmentation,  # poly
#             "area": area,  # segmentation area
#             "iscrowd": 0,
#             "image_id": index,
#             "bbox": [x, y, w, h],
#             "category_id": i,
#             "id": index + 500
#         }

    
#     np.save("info_image_order.npy", info_im)
#     return images_info, labels_info
    


images_info = []
labels_info=[]
index = 1
num = 1000000000000
for i in range (23):
    image_list = os.listdir(in_dir+str(i+1)+'/')
    # images, label = Parallel(n_jobs = num_cores)(delayed(create)(j) for j in range (5))))
    # images_info.append(images)
    # labels_info.app
    for j in range (len(image_list)):
        temp_name = image_list[j]        
        info = [index,temp_name]
        info_im.append(info)

        img = Image.open(in_dir + str(i+1) +'/'+temp_name).convert('L')
        img.save(out_dir + 'COCO_val2014_'+str(index+num)[1:]+'.jpg', 'jpeg')

        img = np.array(img)
        print img.shape, 'de: ', temp_name
        # pdb.set_trace()
        tophat = ndi.white_tophat(img,5)
        otsu = threshold_otsu(tophat)
        mask = (img>otsu).astype(np.uint8)
        im2,contours,hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnt = contours[0]
        M = cv2.moments(cnt)

        x,y,w,h = cv2.boundingRect(cnt)
        segmentation = []
        area = cv2.contourArea(contours[0])

        for contour in contours:
            contour = contour.flatten().tolist()
            segmentation.append(contour)
        
        images_info.append( 
            {
                "license": 1,
                "file_name": 'COCO_val2014_'+str(index+num)[1:]+'.jpg',
                "coco_url": "",
                "height": img.shape[0],
                "width": img.shape[1],
                "date_captured": "ni idea",
                "flickr_url": "",
                "id": index
            },
        )

        labels_info.append(
            {
                "segmentation": segmentation,  # poly
                "area": area,  # segmentation area
                "iscrowd": 0,
                "image_id": index,
                "bbox": [x, y, w, h],
                "category_id": i+1,
                "id": index + 500
            },
        )
        index = index+1

np.save("info_image_order_val.npy", info_im)



    
json_info = []
json_info.append( {"info": {"description": "BioMedLab Dataset",
                             "url": "",
                             "version": "1.0",
                             "year": 2018,
                             "contributor": "",
                             "date_created": "2017/09/01"},
                   "images": images_info,
                   "licenses": [{"url": "",
                                 "id": 1,
                                 "name": "My License"}],
                   "annotations":labels_info,
                   "categories": [{"supercategory": "cariotipo","id": 1,"name": "1"},
                                  {"supercategory": "cariotipo","id": 2,"name": "2"},
                                  {"supercategory": "cariotipo","id": 3,"name": "3"},
                                  {"supercategory": "cariotipo","id": 4,"name": "4"},
                                  {"supercategory": "cariotipo","id": 5,"name": "5"},
                                  {"supercategory": "cariotipo","id": 6,"name": "6"},
                                  {"supercategory": "cariotipo","id": 7,"name": "7"},
                                  {"supercategory": "cariotipo","id": 8,"name": "8"},
                                  {"supercategory": "cariotipo","id": 9,"name": "9"},
                                  {"supercategory": "cariotipo","id": 10,"name": "10"},
                                  {"supercategory": "cariotipo","id": 11,"name": "11"},
                                  {"supercategory": "cariotipo","id": 12,"name": "12"},
                                  {"supercategory": "cariotipo","id": 13,"name": "13"},
                                  {"supercategory": "cariotipo","id": 14,"name": "14"},
                                  {"supercategory": "cariotipo","id": 15,"name": "15"},
                                  {"supercategory": "cariotipo","id": 16,"name": "16"},
                                  {"supercategory": "cariotipo","id": 17,"name": "17"},
                                  {"supercategory": "cariotipo","id": 18,"name": "18"},
                                  {"supercategory": "cariotipo","id": 19,"name": "19"},
                                  {"supercategory": "cariotipo","id": 20,"name": "20"},
                                  {"supercategory": "cariotipo","id": 21,"name": "21"},
                                  {"supercategory": "cariotipo","id": 22,"name": "22"},
                                  {"supercategory": "cariotipo","id": 23,"name": "23"},
                                  {"supercategory": "animal","id": 24,"name": "zebra"},{"supercategory": "animal","id": 25,"name": "giraffe"},{"supercategory": "accessory","id": 27,"name": "backpack"},{"supercategory": "accessory","id": 28,"name": "umbrella"},{"supercategory": "accessory","id": 31,"name": "handbag"},{"supercategory": "accessory","id": 32,"name": "tie"},{"supercategory": "accessory","id": 33,"name": "suitcase"},{"supercategory": "sports","id": 34,"name": "frisbee"},{"supercategory": "sports","id": 35,"name": "skis"},{"supercategory": "sports","id": 36,"name": "snowboard"},{"supercategory": "sports","id": 37,"name": "sports ball"},{"supercategory": "sports","id": 38,"name": "kite"},{"supercategory": "sports","id": 39,"name": "baseball bat"},{"supercategory": "sports","id": 40,"name": "baseball glove"},{"supercategory": "sports","id": 41,"name": "skateboard"},{"supercategory": "sports","id": 42,"name": "surfboard"},{"supercategory": "sports","id": 43,"name": "tennis racket"},{"supercategory": "kitchen","id": 44,"name": "bottle"},{"supercategory": "kitchen","id": 46,"name": "wine glass"},{"supercategory": "kitchen","id": 47,"name": "cup"},{"supercategory": "kitchen","id": 48,"name": "fork"},{"supercategory": "kitchen","id": 49,"name": "knife"},{"supercategory": "kitchen","id": 50,"name": "spoon"},{"supercategory": "kitchen","id": 51,"name": "bowl"},{"supercategory": "food","id": 52,"name": "banana"},{"supercategory": "food","id": 53,"name": "apple"},{"supercategory": "food","id": 54,"name": "sandwich"},{"supercategory": "food","id": 55,"name": "orange"},{"supercategory": "food","id": 56,"name": "broccoli"},{"supercategory": "food","id": 57,"name": "carrot"},{"supercategory": "food","id": 58,"name": "hot dog"},{"supercategory": "food","id": 59,"name": "pizza"},{"supercategory": "food","id": 60,"name": "donut"},{"supercategory": "food","id": 61,"name": "cake"},{"supercategory": "furniture","id": 62,"name": "chair"},{"supercategory": "furniture","id": 63,"name": "couch"},{"supercategory": "furniture","id": 64,"name": "potted plant"},{"supercategory": "furniture","id": 65,"name": "bed"},{"supercategory": "furniture","id": 67,"name": "dining table"},{"supercategory": "furniture","id": 70,"name": "toilet"},{"supercategory": "electronic","id": 72,"name": "tv"},{"supercategory": "electronic","id": 73,"name": "laptop"},{"supercategory": "electronic","id": 74,"name": "mouse"},{"supercategory": "electronic","id": 75,"name": "remote"},{"supercategory": "electronic","id": 76,"name": "keyboard"},{"supercategory": "electronic","id": 77,"name": "cell phone"},{"supercategory": "appliance","id": 78,"name": "microwave"},{"supercategory": "appliance","id": 79,"name": "oven"},{"supercategory": "appliance","id": 80,"name": "toaster"},{"supercategory": "appliance","id": 81,"name": "sink"},{"supercategory": "appliance","id": 82,"name": "refrigerator"},{"supercategory": "indoor","id": 84,"name": "book"},{"supercategory": "indoor","id": 85,"name": "clock"},{"supercategory": "indoor","id": 86,"name": "vase"},{"supercategory": "indoor","id": 87,"name": "scissors"},{"supercategory": "indoor","id": 88,"name": "teddy bear"},{"supercategory": "indoor","id": 89,"name": "hair drier"},{"supercategory": "indoor","id": 90,"name": "toothbrush"}]}
)     

try:
    to_unicode = unicode
except NameError:
    to_unicode = str
    
# print(json.dumps(json_info, indent=4)) 
# json.dump(json_info, '/media/user_home1/lcastillo/biologia/intances_minival2014.json')   instances_train2014.json or instances_minival2014.json
with io.open('/media/user_home1/lcastillo/biologia/instances_train2014.json', 'w', encoding='utf8') as outfile:
    # str_ = json.dumps(json_info,
    #                   indent=0, sort_keys=True,
    #                   separators=(',', ': '), ensure_ascii=False)
    str_ = json.dumps(json_info)
    outfile.write(to_unicode(str_))
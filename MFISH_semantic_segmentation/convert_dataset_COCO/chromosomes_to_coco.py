#!/usr/bin/env python3

import datetime
import json
import os
import re
import fnmatch
from PIL import Image
import numpy as np
from pycococreatortools import pycococreatortools
import pdb

ROOT_DIR = '/home/laubravo/Documents/cariotipos/MFISH_split_binaries/train'
IMAGE_DIR = os.path.join(ROOT_DIR, "train2018")
ANNOTATION_DIR = os.path.join(ROOT_DIR, "annotations")

INFO = {
    "description": "Example MFISH Dataset",
    "url": "https://github.com/jeanpat/MFISH",
    "version": "",
    "year": 2000,
    "contributor": "Wade Schwartzkopf, Advanced Digital Imaging Research",
    "date_created": datetime.datetime.utcnow().isoformat(' ')
}

LICENSES = [
    {
        "id": 1,
        "name": "Attribution-NonCommercial-ShareAlike License",
        "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/"
    }
]

CATEGORIES = [
    {
        'id': 1,
        'name': 'c01',
        'supercategory': 'chromosome',
    },
    {
        'id': 2,
        'name': 'c02',
        'supercategory': 'chromosome',
    },
    {
        'id': 3,
        'name': 'c03',
        'supercategory': 'chromosome',
    },
    {
        'id': 4,
        'name': 'c04',
        'supercategory': 'chromosome',
    },
    {
        'id': 5,
        'name': 'c05',
        'supercategory': 'chromosome',
    },
    {
        'id': 6,
        'name': 'c06',
        'supercategory': 'chromosome',
    },
    {
        'id': 7,
        'name': 'c07',
        'supercategory': 'chromosome',
    },
    {
        'id': 8,
        'name': 'c08',
        'supercategory': 'chromosome',
    },
    {
        'id': 9,
        'name': 'c09',
        'supercategory': 'chromosome',
    },
    {
        'id': 10,
        'name': 'c10',
        'supercategory': 'chromosome',
    },
    {
        'id': 11,
        'name': 'c11',
        'supercategory': 'chromosome',
    },
    {
        'id': 12,
        'name': 'c12',
        'supercategory': 'chromosome',
    },
    {
        'id': 13,
        'name': 'c13',
        'supercategory': 'chromosome',
    },
    {
        'id': 14,
        'name': 'c14',
        'supercategory': 'chromosome',
    },
    {
        'id': 15,
        'name': 'c15',
        'supercategory': 'chromosome',
    },
    {
        'id': 16,
        'name': 'c16',
        'supercategory': 'chromosome',
    },
    {
        'id': 17,
        'name': 'c17',
        'supercategory': 'chromosome',
    },
    {
        'id': 18,
        'name': 'c18',
        'supercategory': 'chromosome',
    },
    {
        'id': 19,
        'name': 'c19',
        'supercategory': 'chromosome',
    },
    {
        'id': 20,
        'name': 'c20',
        'supercategory': 'chromosome',
    },
    {
        'id': 21,
        'name': 'c21',
        'supercategory': 'chromosome',
    },
    {
        'id': 22,
        'name': 'c22',
        'supercategory': 'chromosome',
    },
    {
        'id': 23,
        'name': 'c23',
        'supercategory': 'chromosome',
    },
    {
        'id': 24,
        'name': 'c24',
        'supercategory': 'chromosome',
    },
]

def filter_for_jpeg(root, files):
    file_types = ['*.jpeg', '*.jpg', '*.png']
    file_types = r'|'.join([fnmatch.translate(x) for x in file_types])
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if re.match(file_types, f)]
    
    return files

def filter_for_annotations(root, files, image_filename):
    file_types = ['*.png']
    file_types = r'|'.join([fnmatch.translate(x) for x in file_types])
    basename_no_extension = os.path.splitext(os.path.basename(image_filename))[0]
    file_name_prefix = basename_no_extension + '.*'
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if re.match(file_types, f)]
    files = [f for f in files if re.match(file_name_prefix, os.path.splitext(os.path.basename(f))[0])]

    return files

def main():

    coco_output = {
        "info": INFO,
        "licenses": LICENSES,
        "categories": CATEGORIES,
        "images": [],
        "annotations": []
    }

    image_id = 1
    segmentation_id = 1
    
    # filter for jpeg images
    for root, _, files in os.walk(IMAGE_DIR):
        image_files = filter_for_jpeg(root, files)

        # go through each image
        for image_filename in image_files:
            image = Image.open(image_filename)
            image_info = pycococreatortools.create_image_info(
                image_id, os.path.basename(image_filename), image.size)
            coco_output["images"].append(image_info)

            # filter for associated png annotations
            for root, _, files in os.walk(ANNOTATION_DIR):
                annotation_files = filter_for_annotations(root, files, image_filename)

                # go through each associated annotation
                for annotation_filename in annotation_files:
                    
                    print(annotation_filename)
                    if 'c01' in annotation_filename:
                        class_id = 1
                    elif 'c02' in annotation_filename:
                        class_id = 2
                    elif 'c03' in annotation_filename:
                        class_id = 3
                    elif 'c04' in annotation_filename:
                        class_id = 4
                    elif 'c05' in annotation_filename:
                        class_id = 5
                    elif 'c06' in annotation_filename:
                        class_id = 6
                    elif 'c07' in annotation_filename:
                        class_id = 7
                    elif 'c08' in annotation_filename:
                        class_id = 8
                    elif 'c09' in annotation_filename:
                        class_id = 9
                    elif 'c10' in annotation_filename:
                        class_id = 10
                    elif 'c11' in annotation_filename:
                        class_id = 11
                    elif 'c12' in annotation_filename:
                        class_id = 12
                    elif 'c13' in annotation_filename:
                        class_id = 13
                    elif 'c14' in annotation_filename:
                        class_id = 14
                    elif 'c15' in annotation_filename:
                        class_id = 15
                    elif 'c16' in annotation_filename:
                        class_id = 16
                    elif 'c17' in annotation_filename:
                        class_id = 17
                    elif 'c18' in annotation_filename:
                        class_id = 18
                    elif 'c19' in annotation_filename:
                        class_id = 19
                    elif 'c20' in annotation_filename:
                        class_id = 20
                    elif 'c21' in annotation_filename:
                        class_id = 21
                    elif 'c22' in annotation_filename:
                        class_id = 22
                    elif 'c23' in annotation_filename:
                        class_id = 23
                    else:
                        class_id = 24

                    category_info = {'id': class_id, 'is_crowd': 'crowd' in image_filename}
                    binary_mask = np.asarray(Image.open(annotation_filename)
                        .convert('1')).astype(np.uint8)
                    
                    annotation_info = pycococreatortools.create_annotation_info(
                        segmentation_id, image_id, category_info, binary_mask,
                        image.size, tolerance=2)

                    if annotation_info is not None:
                        coco_output["annotations"].append(annotation_info)

                    segmentation_id = segmentation_id + 1

            image_id = image_id + 1

    with open('{}/MFISH_chromosomes_train2018.json'.format(ANNOTATION_DIR), 'w') as output_json_file:
        json.dump(coco_output, output_json_file)


if __name__ == "__main__":
    main()

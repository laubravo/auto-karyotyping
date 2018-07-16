#matplotlib inline
import argparse
from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import os as os


def parse_args():
    """Parse input arguments"""
    parser = argparse.ArgumentParser(description='Separate annotations into binaries')

    parser.add_argument(
        '--data_dir', dest='data_dir', required=True,
        help='Complete path to chromosome dataset')
    parser.add_argument(
        '--save_dir', dest='save_dir', required=True,
        help='Complete path to save dataset')
    parser.add_argument(
        '--set_name', dest='set_name', required=True,
        help='Set split name of the dataset')
    return parser.parse_args()

# Show all images in set with annotations of all categories

args = parse_args()
print('Called with args:')
print(args)

set_name = args.set_name
image_directory = os.path.join(args.data_dir, args.set_name, args.set_name + '2018')
annotation_file = os.path.join(args.data_dir, args.set_name, 'annotations', 'MFISH_chromosomes_' + args.set_name + '2018.json')
save_directory =  os.path.join(args.save_dir, args.set_name)

if not os.path.exists(save_directory):
    os.makedirs(save_directory)

example_coco = COCO(annotation_file)

categories = example_coco.loadCats(example_coco.getCatIds())
category_names = [category['name'] for category in categories]
category_names = set([category['supercategory'] for category in categories])

print(example_coco)
category_ids = example_coco.getCatIds(catNms=['chromosome'])
image_ids = example_coco.getImgIds(catIds=category_ids)
print(image_ids)
for current_im in image_ids:
    image_data = example_coco.loadImgs(current_im)[0]
    image_data
    # load and display instance annotations
    image = io.imread(os.path.join(image_directory, image_data['file_name']))
    plt.imshow(image); plt.axis('off')
    pylab.rcParams['figure.figsize'] = (8.0, 10.0)
    annotation_ids = example_coco.getAnnIds(imgIds=image_data['id'], catIds=category_ids, iscrowd=None)
    annotations = example_coco.loadAnns(annotation_ids)
    example_coco.showAnns(annotations)
    plt.savefig(os.path.join(save_directory, args.set_name + '_annotation_'+ image_data['file_name']), bbox_inches='tight')
    
    print('Done saving image: ' + str(current_im))
    plt.clf()
    plt.cla()
    plt.close()
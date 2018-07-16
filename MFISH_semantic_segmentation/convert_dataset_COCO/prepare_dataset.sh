#!/bin/bash
DATA_DIR='/media/SSD2/cariotipos/MFISH_Dataset/MFISH_original'
SPLIT_DATA_DIR='/media/SSD2/cariotipos/MFISH_Dataset/MFISH_augmented'
SEPARATE_ANNS_DIR='/media/SSD2/cariotipos/MFISH_Dataset/MFISH_augmented_split'
VISUALIZATIONS_DIR='/media/SSD2/cariotipos/MFISH_Dataset/vis_annotations/MFISH_augmented'

declare -a set_names=('train' 'val' 'test')

python dataset_sorting.py --data_dir $DATA_DIR --save_dir $SPLIT_DATA_DIR

## now loop through the above array
for set in "${set_names[@]}"
do
   python separate_annotations_binaries.py --set_name $set --data_dir $SPLIT_DATA_DIR --save_dir $SEPARATE_ANNS_DIR
   python chromosomes_to_coco.py --set_name $set --data_dir $SEPARATE_ANNS_DIR
done

python visualize_coco_annotations.py --set_name ${set_names[0]} --data_dir $SEPARATE_ANNS_DIR --save_dir $VISUALIZATIONS_DIR

#python separate_annotations_binaries.py --set_name 'train' --data_dir $SPLIT_DATA_DIR --save_dir $SEPARATE_ANNS_DIR
#python chromosomes_to_coco.py --set_name 'train' --data_dir $SEPARATE_ANNS_DIR


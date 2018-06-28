
#To point to dataset first set soft link:
# ln -s path/to/coco data/coco
export CUDA_VISIBLE_DEVICES=0,1,2 

#DATASET_NAME="coco2017"
DATASET_NAME="MFISH_train"
PATH_DETECTRON_WEIGHTS='/home/labravo/Detectron/Detectron.pytorch/data/pretrained_model/resnet_50_C4_1x.pkl'
CONFIG_DIR='../../configs/baselines/e2e_mask_rcnn_R-50-C4_1x.yaml'
ITER_SIZE=1
BATCH_SIZE=3
DATASET_DIR='/media/SSD2/Detectron/data'

# no finetuning
#python train_net_step.py --set 'DATA_DIR' $DATASET_DIR --cfg $CONFIG_DIR --dataset $DATASET_NAME --iter_size $ITER_SIZE --bs $BATCH_SIZE 

# finetunning
python train_net_step_modifications.py --set 'DATA_DIR' $DATASET_DIR --cfg $CONFIG_DIR --dataset $DATASET_NAME --iter_size $ITER_SIZE --bs $BATCH_SIZE --load_detectron $PATH_DETECTRON_WEIGHTS

#python train_net.py --cfg $CONFIG_DIR --dataset $DATASET_NAME --load_detectron $PATH_DETECTRON_WEIGHTS --ckpt_num_per_epoch $NUM_CKPT_PER_EPOCH --epochs $NUM_EPOCH


# code for modifying nets taken from: https://github.com/floydhub/imagenet/blob/master/main.py

# train model

# MODEL_NAME options: alexnet, densenet121, inceptionv3, resnet18, resnet34, resnet50, resnet101, vgg11, vgg16, vgg11_bn, vgg16_bn

LR=0.001
BATCH_SIZE=80

PATH_TO_MAIN='/home/labravo/cariotipos/auto-karyotyping/classification-net/pytorch_code'
MODEL_NAME='densenet121'
NUM_EPOCHS=1000
PATH_TO_DATASET='/media/SSD2/cariotipos/classification-net/classificationDB'
EXPERIMENT_NAME=$MODEL_NAME'_'$NUM_EPOCHS'epochs_lr'$LR'_batch_size'$BATCH_SIZE
SAVE_DIR="/media/SSD2/cariotipos/classification-net/"$EXPERIMENT_NAME

mkdir $SAVE_DIR

GPU_NUM=1 #0 o 2
export CUDA_VISIBLE_DEVICES=$GPU_NUM

python "$PATH_TO_MAIN/main.py" -a $MODEL_NAME --lr $LR -b $BATCH_SIZE --epochs $NUM_EPOCHS --pretrained --print-freq 10 $PATH_TO_DATASET --saveDir $SAVE_DIR -t

# test model

BATCH_SIZE=1
PATH_TO_MODEL=$SAVE_DIR'model_best.pth.tar'

python "$PATH_TO_MAIN/main.py" -a $MODEL_NAME -b $BATCH_SIZE --pretrained --print-freq 10 --resume $PATH_TO_MODEL --saveDir $SAVE_DIR -e $PATH_TO_DATASET -t

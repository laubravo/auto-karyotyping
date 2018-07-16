# MFISH dataset Semantic Segmentation
Semantic segmentation is achieved via [Detectron for PyTorch](https://github.com/roytseng-tw/Detectron.pytorch). 

For installation use:  
https://github.com/andfoy/Detectron.pytorch
In the brach root write:  
```
pip install . --no-deps
```
## Converting Dataset into COCO format
Install [pycococreator](https://github.com/waspinator/pycococreator/) with 
```
pip install git+git://github.com/waspinator/pycococreator.git@0.2.0
```
Then check that the dataset information including class names and ids in convert_dataset_COCO/chromosomes_to_coco.py correspond to dataset  
For this to work dataset must be in format specified by pycococreator. The script convert_dataset_COCO/separate_annotations_binaries.py helps with the annotation format.  

To check that dataset was correctly converted into COCO format visualize them with convert_dataset_COCO/visualize_coco.ipynb. This Jupyter Notebook uses the [COCO API pycocotools](https://github.com/cocodataset/cocoapi)

## Modifying Detectron for the MFISH dataset
The process followed what was outlined in this [issue](https://github.com/roytseng-tw/Detectron.pytorch/issues/60).  
1. Convert dataset to COCO format  
2. Add dataset to the ``` lib/datasets/dataset_catalog.py ```  
3. Modify available options for dataset names in ``` tools/train_net_step.py ``` (dataset was added as MFISH_train). This change can be found in the repo's ```scripts/train_net_step_modifications.py``` script.
4. Modify the .yaml file if it has a ```NUM_CLASSES``` item. Note: the number of classes must account for the background class so it should be one more than the number defined in 0.
5. Adjust the net's output layers to fit the new number of classes. A preliminary version of this change can be found in the repo's ```scripts/train_net_step_modifications.py``` script.

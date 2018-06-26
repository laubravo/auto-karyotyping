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

To check that dataset was correctly converted into COCO format visualize them with convert_dataset_COCO/visualize_coco.ipynb

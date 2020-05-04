# Installation
pull the Mask R-CNN repo and install it 
`git clone https://github.com/matterport/Mask_RCNN.git`
```
cd Mask_RCNN
python setup.py install
```
Download [model weights](https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5)

`conda create --name <env> --file requirements.txt`

## Updating Requirements
`conda list -e > requirements.txt`


#### References
https://machinelearningmastery.com/how-to-perform-object-detection-in-photographs-with-mask-r-cnn-in-keras/
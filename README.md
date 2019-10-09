# IkeaProductClassification
Project to identify products from IKEA product categories.

## Data

- This project has data scraped from IKEA on four different classes:

    - **Chairs**
    ![Chairs](https://i.imgur.com/Aa1D8ME.png)
    
    - **Beds**
    ![Beds](https://i.imgur.com/AayLhPC.png)
    
    - **Candle Holders**
    ![Candle Holders](https://i.imgur.com/MUkcW3a.png)
    
    - **Wardrobes**
    ![Wardrobes](https://i.imgur.com/OPx8SNS.png)


- There are total 2,421 product images in data/model_data directory. However,
Images scrapped alone from IKEA website (using src/FetchData.py) for each product category is 
not enough to train a multiclass classifier using a pretrained model.
- Hence additional data scraped from google images  has been added 
to raise number of samples per class at least to 400 images(Images from
google images were downloaded using [Download all Images](https://chrome.google.com/webstore/detail/download-all-images/nnffbdeachhbpfapjklmpnmjcgamcdmm?hl=en)
 chrome extension).
- Scrapped data is split into train and validation datasets where
validation data has atleast 40 samples per each class

## Requirements
- **fastai** library, you can install it with pip

        `pip install fastai`
        
- **Python3.6**
- Selenium
- All dependencies can be installed by running
    
        `pip install -r requirements.txt`

## Data preprocessing
- Images are standardized by using ImageNet data mean and standard deviations.

### Data Augmentations used
- random_flip: with p=0.5
- rotate: between -10 to 10 degrees
- zoom
- lightning variations
- wrapping

## Training a multi-class classifier
### Why ResNext_50?
- In general ResNet based architectures are found to generalise better
on custom datasets.
- ResNext based architecture has a higher model capacity at parameter
cost almost equivalent to ResNet based equivalent architecture

### Model specifications
- ResNext_50(R50) pretrained is used as a classifier.
- Model is defined and trained using src/ResNext_50.ipynb
- For transfer learning, the ImageNet specific FC layer of the R50 is removed and replaced
with the following layers 
    - AdaptiveAvgPool2d
    - AdaptiveMaxPool2d
    - Flatten
    - BatchNorm1d
    - Dropout(p=0.25)
    - FC (512 units)
    - ReLU
    - BatchNorm1d
    - Dropout(p=0.5)
    - FC(4 units)
- R50 is trained for 20 epochs using one cycle learning rate policy

## Train model on IKEA data
- To train the model use src/ResNext_50.ipynb notebook
- If you are unable to see the notebook in github, you can open it in colab [here](https://colab.research.google.com/drive/1ehv7IZ46BqrZgVjZGvJdN9qad_RAVCHo)

## Training and Validation loss
![Training and Validation loss](https://i.imgur.com/8NPrwwM.png)

## Confusion matrix
![confusion matrix](https://i.imgur.com/iOg8h8v.png)

## Interpreting model predictions

![Predictions](https://i.imgur.com/1ZHuIbs.png)

As it can be clearly seen the first and second are wrong predictions. 
- However, in the first example even though the actual label is **Bed** model predicts it as charis
 because this product looks like a sofa, convertable to bed and it also shares lot of common 
 features with chairs class.

<p align="center"> 
<img src="https://i.imgur.com/tz6fen2.png">
</p>

- In second prediction, model is predicting as wardrobe because of the 
background in the image which do have a mini shelf structure similar to wardrobe.

<p align="center"> 
<img src="https://i.imgur.com/b1MdWma.png">
</p>


## Model weights
Model weights are saved to data/models dir when model.save('model_name'') is performed
in src/ResNext_50.ipynb


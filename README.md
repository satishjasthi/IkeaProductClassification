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

## Training a multi-class classifier
- ResNext_50(R50) pretrained is used as a classifier.
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

## Training and Validation loss
![Training and Validation loss](https://i.imgur.com/8NPrwwM.png)

## Confusion matrix
![confusion matrix](https://i.imgur.com/iOg8h8v.png)

## Interpreting model predictions

![Predictions](https://i.imgur.com/GQ3o2ks.png)

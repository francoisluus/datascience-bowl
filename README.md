Python start guide for data science bowl
----------------------------------------

The following set of scripts should be a good way to get started with
[Convolution Neural
Networks](http://en.wikipedia.org/wiki/Convolutional_neural_network).  It uses
a [GraphLab-Create's deep
learning](https://dato.com/learn/userguide/#neural-net-classifier) which is
based on CXXNet.

This attempt is a modified version of https://github.com/srikris/datascience-bowl.
https://github.com/srikris/datascience-bowl achieved a Public Leaderboard score of 0.93.

* **Setup time**: ~30 mins
* **Train and submit creation time**: ~3 hours 40 mins on a GRID K520 GPU
* **Validation score**: 0.84 (72%)
* **Public Leaderboard score**: 0.85


Solution
--------

Here is a quick summary of the submission:

* Load images into an SFrame (scalable dataframe).
* Use [Pillow](https://pypi.python.org/pypi/Pillow/) to augment the data with
  rotations with angle 90, 180, and 270.
* Setup a simple deep learning architecture (based on
  [antinucleon](https://github.com/antinucleon/cxxnet/blob/master/example/kaggle_bowl/bowl.conf]))
* Create a "fair" train, validaiton split to make sure the classes are balanced.
* Train a deep learning model.
* Evaluate the multi-class log loss score.
* Save the predictions in Kaggle's format into a submission file called "submission.csv".


Install
-------
**CPU instructions**
```
pip install -r requirements.pip
```

**GPU instructions**
```
pip install -r requirements-gpu.pip
```

Data
-----
Let us assume that you have the data downloaded into two folders called train 
and test. You can do that as follows: (You will probably need a cookie file,
so just download it from the website.)

```
wget https://www.kaggle.com/c/datasciencebowl/download/train.zip
wget https://www.kaggle.com/c/datasciencebowl/download/test.zip
wget http://www.kaggle.com/c/datasciencebowl/download/sampleSubmission.csv.zip
unzip train.zip
unzip test.zip
unzip sampleSubmission.csv.zip
```

Morphological dataset
-----
Use the grayscale images in train/ and test/ to produce RGB images that
consist of 3 channels, the original grayscale image and two basic morphological
operations on the original images, like tophat and bottomhat.

Use gen_train.py and gen_test.py to create a new dataset, change the folder
locations to match your train/ and test/ parent directory.

Train dataset creation: 5 minutes
```
python gen_train.py
```

Test dataset creation: 25 minutes
```
python gen_test.py
```

Make submission
---------------

Now run the following script. The script will create a submission file.
Change the folder locations in the script to point to your new morphological
dataset locations, and to the unzipped sampleSubmission.csv

```
python make_submission.py
```

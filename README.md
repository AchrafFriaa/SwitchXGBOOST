# Contactless Multi-Array Switch

![ScreenShot](https://raw.github.com/AchrafFriaa/SwitchXGBOOST/master/img/20201210_142639.jpg)

### The application kit contains :

* Multi-Array Switch add-on, consisting of 4 magnets that can be moved contactles into two different states. 16 different states in total are therefore possible. Magnets are included.

* The additional needed 3D2Go board or the 3D shield can be used for the read-out.

With a magnetic 3D sensor a contactless multi-array switch can be generated. In this example, four independent moving magnets create unique magnetic fields indicating 16 different switching combinations.
This can be used as a Human-Machine-Interface and has no tear or wear to the sensing element.


## Code Summary :

The multiswitch code contains the following files:

1. data.txt
2. dataCollection.py
3. main.py

## Dependencies: 

```bash
pip install {lib}

```
* numpy
* pyserial
* xgboost
* bitstring
* pandas
* sklearn

## Data collection and preprocessing

This program uses a machine learning algorithm to predict the exact multiswitch array combination. Data needs to be collected and then feeded to the XGBOOST algorithm to train on it. We provide a ready training dataset in data.txt. 
Run dataCollection.py and follow the instructions if you want to create your own dataset or extend the already existing one.

## Array combination

Finally, run main.py to predict the array combination. When trained on the provided data, an accuracy of 95% (+- 3%) is achieved. You can play with the algorithm's hyperparameters and feed more data to it to further improve the accuracy.  

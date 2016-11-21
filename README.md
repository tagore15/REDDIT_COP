# REDDIT COP

This repository contains my attempts to predict popularity of reddit posts till now. Data set is taken from: https://github.com/umbrae/reddit-top-2.5-million.  
To run current status of app, run search.py after copying data folder in running directory.

Files description are: 

## app_engine  
This was intended for creating a running web app in google app engine.  
I was able to run engine on local host, but could not upload it on server seemingly due to app engine space limitations. Also I later found out that sklearn is not supported in app engine.
For now, user would need to run python script search.py to interact with app. 


## search.py
This script create index for search engine on the basis of title fields in csv file. Prediction API could not be integerated till now due to lack of stand-alone pandas installation on my system. Model is created in ipython notebook. This scipt also provides interface to user for entering query.   

## model.ipynb
This files demonstrate my attemps to create model. Models' features are created using processed title text  with tf-idf vectorizer. I chose 500 random subreddits for training and 500 other subreddits for testing. We still need to finetune the model by attempting other regressors and hyper parameters tuning using grid search. We should also choose other features than title by using one-hot encoding.

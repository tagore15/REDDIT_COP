# import needed modules
import os
import glob
import csv
import io

index = {}
print("\nCREATING SEARCH INDEX (It would take few minutes)_ _ _ _\n")
# create list of csv files
import glob
path =r'data' # use your path
fileList = glob.glob(path + "/*.csv")

# create index by reading csv files
for filename in fileList:
    #with .open(filename, encoding="utf-8") as f:
    with open(filename) as f:
        reader = csv.reader(f)
        your_list = list(reader)
        for lst in range(len(your_list)):
            if lst == 0:
                continue  # skipping header
            word = your_list[lst][4].split()
            for w in word:
                w = w.lower()
                if w not in index:
                    index[w] = [(filename, lst, int(your_list[lst][1]))]
                else:
                    index[w].append((filename, lst, int(your_list[lst][1])))

# sort the results
for idx in index.keys():
    index[idx] = sorted(index[idx], key=lambda ind:ind[2], reverse = True)
print("SEARCH INDEX CREATED.....")

def readNthLine(fileName, lineNum):
    with open(fileName) as f:
        reader = csv.reader(f)
        your_list = list(reader)
        return ','.join(your_list[lineNum])

"""
COMMENTING OUT AS NEEDS INSTALLATION OF PANDAS TO RUN BELOW CODE
FOR NOW USING IPYTHON FOR TRAINING MODEL

print("TRAINING MODEL.....")
# score predictor
# training model
# select 500 random files
import random
trainFiles = random.sample(range(len(fileList)), 500)
import pandas
frame = pandas.DataFrame()
list_ = []
for file_ in trainFiles:
    df = pandas.read_csv(fileList[file_],index_col=None, header=0)
    list_.append(df)
frame = pandas.concat(list_)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
count_vect = CountVectorizer(stop_words='english')
X_train_counts = count_vect.fit_transform(frame['title'])
tf_transformer = TfidfTransformer().fit(X_train_counts)
X_train_counts_tf = tf_transformer.transform(X_train_counts)
X_train_out = frame['score']
from sklearn.tree import DecisionTreeRegressor
reg = DecisionTreeRegressor(max_depth = 25)
reg.fit(X_train_counts_tf, X_train_out)
from sklearn.metrics import mean_squared_error
X_train_predict = reg.predict(X_train_counts_tf)
# check training error
train_error = mean_squared_error(X_train_out, X_train_predict)

#check testing error
# check mean squared error on 500 different subreddits than used for training
frame_test = pandas.DataFrame()
list_ = []
for file_ in range(len(fileList)):
    if file_ not in trainFiles:
        df = pandas.read_csv(fileList[file_],index_col=None, header=0)
        list_.append(df)
    if len(list_) == 500:
        break
frame_test = pandas.concat(list_)
X_test_out = frame_test['score']
X_test_counts = count_vect.transform(frame_test['title'])
X_test_counts_tf = tf_transformer.transform(X_test_counts)
X_test_predict = reg.predict(X_test_counts_tf)
test_error = mean_squared_error(X_test_out, X_test_predict)
print("\nTRAINING ERROR ON 500 RANDOM SUBREDDIT: {}".format(train_error))
print("\nTESTING ERROR ON 500 RANDOM SUBREDDIT: {}".format(test_error))

def predictScore(fileName, lineNum):
    dfp = pandas.read_csv(fileName, index_col=None, header=0)
    X_counts = count_vect.transform(dfp['title'])
    X_counts_tf = tf_transformer.transform(X_counts)
    X_predict = reg.predict(X_counts_tf)
    return X_predict[lineNum]
"""
def searchString(keyword):
    results = "" 
    if keyword not in index:
        results += "string not found"
    else:
        results = "TOP 10 RESULTS" 
        for (fileName, lineNum, score) in index[keyword][:10]:
            results += ("\n\n====== SUBREDDIT: {}, ACTUAL SCORE: {} PREDICTED SCORE: {} ========\n".format(fileName, score, 0))
            results += readNthLine(fileName, lineNum)
    return results

# UI for getting search string
while True:
    in_search = raw_input("\nEnter word you want to search: ")
    in_search = in_search.lower()
    results = searchString(in_search)
    print(results)

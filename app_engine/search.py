# import needed modules
import os
import glob
import csv
import io

index = {}

# create list of csv files
import glob
path =r'data' # use your path
fileList = glob.glob(path + "/*.csv")
#my_dir = "H:\\REDDIT\\DATA\\reddit-top-2.5-million\\data"
#fileList = []
#os.chdir(my_dir)
#for files in glob.glob("*.csv"):
#    fileList.append(files)
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

def readNthLine(fileName, lineNum):
    with open(fileName) as f:
    	reader = csv.reader(f)
	your_list = list(reader)
	return ','.join(your_list[lineNum])

def searchString(keyword):
    results = "" 
    if keyword not in index:
    	results += "string not found"
    else:
    	for (fileName, lineNum, score) in index[keyword][:10]:
    	    results += ("====== SUBREDDIT: {}, SCORE: {} ========".format(fileName, score))
            results += readNthLine(fileName, lineNum)
    return results

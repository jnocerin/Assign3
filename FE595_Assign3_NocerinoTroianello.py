# Import package statements
import matplotlib as matplotlib
from requests import get
import time
import re
import glob
import os
os.chdir('/Users/jessica.troianello/PycharmProjects/Assign3')
import fileinput
import shutil

#Read all male files and merge into 1 file

Moutfilename = 'maleHeros.txt'
with open(Moutfilename, 'wb') as outfile:
    for filename in glob.glob("Extracted/Male/*.txt"):
        if filename == Moutfilename:
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
    outfile.close()

# #Read all female files and merge into 1 file
Foutfilename = 'femaleHeros.txt'
with open(Foutfilename, 'wb') as outfile:
    for filename in glob.glob("Extracted/Female/*.txt"):
        if filename == Foutfilename:
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
    outfile.close()

# create loop to clean data (remove . , and extra text

#Clean Female file

file1 = open('femaleHeros.txt', 'r')
file2 = open('femaleHeros_noperiod.txt', 'w')
file1_cont = file1.readlines()
for line in file1_cont:
    line = line.strip("0123456789.-:,'!")
    line = line.replace('.', '')
    line = line.replace("\\'s", "'s")
    line = line.replace("\\'t", "'t")
    line = line.replace('an ', 'a')
    line = line.replace("She's", '')
    line = line.lstrip()
    line = line.replace("They fight crime!", '')
    line = line.replace("Circus", '')
    line = line.replace("</P>", '')
    file2.write(line)

#Clean Female file

file11 = open('maleHeros.txt', 'r')
file22 = open('maleHeros_noperiod.txt', 'w')
file11_cont = file11.readlines()
for line in file11_cont:
    line = line.strip("0123456789.-:,'!")
    line = line.replace('.', '')
    line = line.replace("\\'s", "'s")
    line = line.replace("\\'t", "'t")
    line = line.replace('an ', 'a')
    line = line.replace("She's", '')
    line = line.lstrip()
    line = line.replace("They fight crime!", '')
    line = line.replace("Circus", '')
    line = line.replace("</P>", '')
    line.split(",")
    file22.write(line)


# abc = open("femaleHeros_nopreiod.txt", "r")
# for line in file:
#     print line

# Run textblob to find sentement of each superhero descriptor and sort by sentement




import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pprint import pprint
analyser = SentimentIntensityAnalyzer()
def sentiment_analysis(text):
    return analyser.polarity_scores(text)
def file_read(fname):
    content_array = []

    with open(fname) as f:
        # Content_list is the list that contains the read lines.
        for line in f:
            map(lambda f: str.replace(f, '\n', ','), content_array)
            content_array.append(line + "," + str(sentiment_analysis(line)) )

 #           content_array = content_array.replace("\n", ',')
 #           content_array.append(sentiment_analysis(line))
        return(content_array)

#        print(content_array.nlargest(10, "Sentiment"))


file3 = open('femaleHeros_withSent.txt', 'w')



output_array = file_read('femaleHeros_noperiod.txt')
pprint(output_array)
with open ('femaleHeros_withSent.txt', 'w') as filehandle:
    for listitem in output_array:
        filehandle.write('%s\n' % listitem)


fileIn = open('femaleHeros_withSent.txt', 'r')
fileOut = open('femaleHeros_toSort.txt', 'w')
file_cont = fileIn.readlines()
for line in file_cont:

    line = line.replace('{', '')
    line = line.replace('}', ',')
#   line = line('\n', '')
    fileOut.write(line)


#file3.write(output_array)

# import pandas as pd
# named_columns = ['Heros', 'Neg', 'Neu', 'Comp']
# dfObj = pd.DataFrame(output_array, columns=named_columns)
# print("Dataframe : " , dfObj, sep=',')
# dfObj.sort_values(by="Comp")
#
#
#
# #file3.write(output_array)
# def custom_sort(t):
#     return t[1]


#dfObj.sort(key=custom_sort)
# pprint(output_array)


# Create Variable of top 10 male and femal and bottom 10 male and female
from textblob import TextBlob
# import sys
# from importlib import reload
# from collections import Counter
# reload(sys)
# sys.getdefaultencoding() # use this for Python3
# from textblob import TextBlob
# url ='femaleHeros_noperiod.txt'
# file=open(url)
# t=file.read()
# print(type(t))
# bobo = TextBlob(t)
# counts = Counter(bobo.sentences)
# print(counts)

#for np in bobo.noun_phrases:
#    print(np)

# import nltk
# from nltk.collocations import *
# bigram_measures = nltk.collocations.BigramAssocMeasures()
# trigram_measures = nltk.collocations.TrigramAssocMeasures()
#
# # change this to read in your data
# finder = BigramCollocationFinder.from_words('femaleHeros_noperiod.txt')
#
# # only bigrams that appear 3+ times
# finder.apply_freq_filter(3)
#
# # return the 10 n-grams with the highest PMI
# finder.nbest(bigram_measures.pmi, 10)
# # Run code to ID most common descriptors and count of occurance


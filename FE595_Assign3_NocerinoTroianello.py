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
import csv
import pandas as pd
import jinja2

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
    line = line.replace("savage, blood-crazed", "savage blood crazed rage")
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
    line = line.replace("savage, blood-crazed", "savage blood crazed rage")
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
# pprint('this is output array')
# pprint(output_array)
# pprint('this end of is output array')


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

workfile  = open('femaleHeros_toSort.txt', 'r')
workfile_cont=workfile.readlines()

strWork = ''.join(output_array)
# clean up text file
remap = {
#    ord('\'') : '',
#    ord(' ') : '',
    ord('{') : '',
    ord('}') : ','
}

cleaned_text = strWork.translate(remap)

# remove tags of values
f_test = re.sub( ",(neg:|neu:|pos:|compound:)", ',', cleaned_text )

# break text into list
string_to_list = f_test.split(',')

# create list of lists with
# list comprehension.
# Each inner list contains
# 5 elements, such as
# 'Subject', 'Neg','Neu','Pos','Compound'

list_to_df = [ string_to_list[i : i + 5] for i in range(0, len(string_to_list), 5) ]
pprint(list_to_df)

# generate pandas dataframe
df = pd.DataFrame(list_to_df, columns = ['Subject', 'Neg','Neu','Pos','Compound'])
#print("dataframe")
#pprint(df)
export_csv=df.to_csv('text.csv',index = None, header=True)
# sort dataframe based on Compound
df_sorted = df.sort_values(['Compound'],
                 ascending = False
                 )
#print("sorted")
#pprint(df_sorted)
pprint ("The top female superheros are :")
pprint(df_sorted.style)
pprint(df_sorted.ix[10:])
# finaldata = []
#
# with open('femaleHeros_toSort.txt', 'r') as in_file:
#     c_reader = csv.reader(in_file, delimiter=',')
#     for row in c_reader:
#         this_row = []
#
#         # from each row, get the name first, stripping the leading and trailing ' single quotes.
#         this_row.append(row[0])
#
#         # get the remaining values
#         for i in range(1, len(row)):
#         # all values appear after a ': ' pattern, in the same order. split on ': '
#         # and get the second half of the split - it's the value we're looking for
#             this_row.append(row[i].split(": ", 1)[1])
#
#         # add this to the array
#         finaldata.append(this_row)
#
#         # make a dataframe out of the csv file
# df = pd.DataFrame(finaldata, columns=['Hero', 'Neg', 'Neu', 'Pos', 'Compound'])
# print(df)





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


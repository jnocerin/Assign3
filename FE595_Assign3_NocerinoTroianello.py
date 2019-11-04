# Import package statements
import glob
import os
import re

os.chdir('/Users/jessica.troianello/PycharmProjects/Assign3')
import shutil
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pprint import pprint
from textblob import TextBlob
import operator

# Set display and print
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)
pd.set_option('display.float_format', '{:20,.2f}'.format)
pd.set_option('display.max_colwidth', -1)

# Read all male files and merge into 1 file

Moutfilename = 'maleHeros.txt'
with open(Moutfilename, 'wb') as outfile:
    for filename in glob.glob("Extracted/Male/*.txt"):
        if filename == Moutfilename:
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
    outfile.close()

# Read all female files and merge into 1 file
Foutfilename = 'femaleHeros.txt'
with open(Foutfilename, 'wb') as outfile:
    for filename in glob.glob("Extracted/Female/*.txt"):
        if filename == Foutfilename:
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
    outfile.close()

# create loops to clean data

# Clean Female file and write to new file

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
    line = line.replace("They fight crime!", '')
    line = line.replace("Circus", '')
    line = line.replace("</P>", '')
    line = line.lstrip()
    file2.write(line)

# Clean Male file and write to new file

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
    line = line.replace("They fight crime!", '')
    line = line.replace("Circus", '')
    line = line.replace("</P>", '')
    line = line.lstrip()
    line.split(",")  # Investigate
    file22.write(line)

# Run sentement of each superhero descriptor and write to new file
# Process Female Heros
file3 = open('femaleHeros_withSent.txt', 'w')  # create new file to write to with sentiment
analyser = SentimentIntensityAnalyzer()


def sentiment_analysis(text):
    return analyser.polarity_scores(text)


# method to read line and add sentiment
def file_read(fname):
    content_array = []
    with open(fname) as f:
        # Content_list is the list that contains the read lines.
        for line in f:
            map(lambda f: str.replace(f, '\n', ','), content_array)
            content_array.append(line + "," + str(sentiment_analysis(line)))
        return (content_array)


output_array = file_read('femaleHeros_noperiod.txt')  # Call method to read and append sentiment into array
# write array to file
with open('femaleHeros_withSent.txt', 'w') as filehandle:
    for listitem in output_array:
        filehandle.write('%s\n' % listitem)

# Do additional clean up following append of sentiment
fileIn = open('femaleHeros_withSent.txt', 'r')
fileOut = open('femaleHeros_toSort.txt', 'w')
file_cont = fileIn.readlines()
for line in file_cont:
    #    line = line.replace('{', '')
    line = line.replace('}', ',')
    fileOut.write(line)

# pull file into a datastore to manupulate and sort with column headers
workfile = open('femaleHeros_toSort.txt', 'r')
workfile_cont = workfile.readlines()

strWork = ''.join(output_array)
# clean up text file
remap = {
    ord('{'): '',
    ord('}'): ','
}

cleaned_text = strWork.translate(remap)

# remove tags of values from Sentiment analysis
f_test = re.sub(",(neg:|neu:|pos:|compound:)", ',', cleaned_text)

# break text into list
string_to_list = f_test.split(',')

# create list of lists with
# list comprehension.
# Each inner list contains
# 5 elements, such as
# 'Subject', 'Neg','Neu','Pos','Compound'

list_to_df = [string_to_list[i: i + 5] for i in range(0, len(string_to_list), 5)]

# generate pandas dataframe with headers
df = pd.DataFrame(list_to_df, columns=['Subject', 'Neg', 'Neu', 'Pos', 'Compound'])
# save to CSV file
export_csv = df.to_csv('CleanedDataFrame.csv', index=None, header=True)

# sort dataframe based on Compound Score
df_sorted = df.sort_values(['Compound'],
                           ascending=False
                           )
export_csv_sorted = df_sorted.to_csv('SortedDataFrame.csv', index=None, header=True)
pprint("The top female superheros are :")
# pprint(df_sorted.iloc[10:])
pprint(df_sorted.head(10))
pprint("The bottom female superheros are : ")
pprint(df_sorted.tail(10))

# Process Male Heros
file33 = open('maleHeros_withSent.txt', 'w')  # create new file to write to with sentiment

output_array3 = file_read('maleHeros_noperiod.txt')  # Call method to read and append sentiment into array
# write array to file
with open('maleHeros_withSent.txt', 'w') as filehandle:
    for listitem in output_array3:
        filehandle.write('%s\n' % listitem)

# Do additional clean up following append of sentiment
fileIn3 = open('maleHeros_withSent.txt', 'r')
fileOut3 = open('maleHeros_toSort.txt', 'w')
file_cont3 = fileIn.readlines()
for line in file_cont3:
    #   line = line.replace('{', '')
    line = line.replace('}', ',')
    fileOut.write(line)

# pull file into a datastore to manupulate and sort with column headers
workfile3 = open('maleHeros_toSort.txt', 'r')
workfile_cont3 = workfile.readlines()

strWork3 = ''.join(output_array)
# clean up text file
remap = {
    ord('{'): '',
    ord('}'): ','
}

cleaned_text = strWork3.translate(remap)

# remove tags of values from Sentiment analysis
m_test = re.sub(",(neg:|neu:|pos:|compound:)", ',', cleaned_text)

# break text into list
string_to_list3 = m_test.split(',')

# create list of lists with
# list comprehension.
# Each inner list contains
# 5 elements, such as
# 'Subject', 'Neg','Neu','Pos','Compound'

list_to_df3 = [string_to_list3[i: i + 5] for i in range(0, len(string_to_list3), 5)]

# generate pandas dataframe with headers
df3 = pd.DataFrame(list_to_df3, columns=['Subject', 'Neg', 'Neu', 'Pos', 'Compound'])
# save to CSV file
export_csv = df3.to_csv('CleanedDataFrameM.csv', index=None, header=True)

# sort dataframe based on Compound Score
df_sorted3 = df3.sort_values(['Compound'],
                             ascending=False
                             )
export_csv_sorted3 = df_sorted.to_csv('SortedDataFrameM.csv', index=None, header=True)
pprint("The top male superheros are :")
# pprint(df_sorted.iloc[10:])
pprint(df_sorted3.head(10))
pprint("The bottom male superheros are : ")
pprint(df_sorted3.tail(10))

# # Run code to ID most common descriptors and count of occurance for Females

#Create object of just female Heros
newForCountsFemale = df_sorted.filter(['Subject'])
# pprint(newForCountsFemale)
# var1 = newForCountsFemale.loc[0:0,'Subject':'Subject']
var1 = newForCountsFemale['Subject']
var2 = newForCountsFemale.to_string(index=False)
workingData = TextBlob(var2)

# Create method that can extract words and count occurances
def word_phase_count(str):
    counts = dict()
    word_phase = str.split()

    for word in word_phase:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


wordOut = word_phase_count(workingData)

nps = workingData.np_counts
nps2 = workingData.noun_phrases

# Sort by occurance
#pprint(wordOut)
#pprint(type(wordOut))
sortOut = sorted(wordOut.items(), key=operator.itemgetter(1), reverse=True)
#for elm in sortOut:
#    print(elm)
#print(type(sortOut))
# Create variable with top 10 (excluding base words)
FinalPush = sortOut[13:24]
#print(FinalPush)
#print(type(FinalPush))

pprint("The top 10 most used descriptors in Female Heros are :")
for key, value in FinalPush:
    print(key, value)

# Run code to ID most common descriptors and count of occurance for Males
#Create object of just femaile Heros
newForCountsMale = df_sorted3.filter(['Subject'])
# pprint(newForCountsFemale)
# var1 = newForCountsFemale.loc[0:0,'Subject':'Subject']
var13 = newForCountsMale['Subject']
var23 = newForCountsMale.to_string(index=False)
workingData3 = TextBlob(var23)

wordOut3 = word_phase_count(workingData3)

nps3 = workingData3.np_counts
nps23 = workingData3.noun_phrases

# Sort by occurance
#pprint(wordOut3)
#pprint(type(wordOut3))
sortOut3 = sorted(wordOut3.items(), key=operator.itemgetter(1), reverse=True)
#for elm3 in sortOut3:
#    print(elm3)
#print(type(sortOut))
# Create variable with top 10 (excluding base words)
FinalPush3 = sortOut3[14:25]
#print(FinalPush3)
#print(type(FinalPush))


pprint("The top 10 most used descriptors in Male Heros are :")
for key, value in FinalPush3:
    print(key, value)
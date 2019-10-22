# Import package statements
from requests import get
import time
import re

# Create RegEX for male value
mal_regex = re.compile(r"(?<=He's)(.*)(?=. She's)")
# Create RegEX for female value
fem_regex = re.compile(r"(?<=She's )(.*)(?=. They fight crime!)")

#Create loop to open and append all files
# create loop to clean data
# run NN to find sentement of each superhero descriptor and sort by sentement
#create Variable of top 10 male and femal and bottom 10 male and female
# run code to ID most common descriptors and count of occurance



#For loop to run extraction 50 times
for i in range (0,50):
    # Open (create if needed) the two files for Append writing
    male = open("maleFile.txt", "a+")
    female = open("femaleFile.txt", "a+")

    # scrape site
    resp = get("http://www.theyfightcrime.org")

    # store scrape as text
    toParse = resp.text

    # Extract male value to variable
    maleVal = mal_regex.search(toParse)

    # Extract female value to variable
    femalVal = fem_regex.search(toParse)

    # Append male value to file
    male.write(maleVal.group())

    # Insert and new line
    male.write("\n")

    # Append female value to variable
    female.write(femalVal.group())

    # Insert a new line
    female.write("\n")

    # close male file
    male.close()

    # Close female file
    female.close()

    # Sleep 5 ms
    time.sleep(5 / 1000)

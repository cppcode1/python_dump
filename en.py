"""
this script translates a word from English to Polish and vice versa. it supplies a
transcription as well. all you have to do it type

python3 en.py en-pl word

dependencies
 2007  inst python3-pip
 2008  pip3  install beautifulsoup4
 2009  pip3 install lxml
 2010  pip3 install requests
alias en="python3 ~/en.py en-pl "
"""
import os
import requests
import sys
import re
from bs4 import BeautifulSoup

os.system("clear")

arguments_count = len(sys.argv)
if  arguments_count == 1:
    print("too little arguments")
    print("python3 en.py(1) en-pl(2) words(3+)")
    exit(0)

direction = sys.argv[1]
#convert from list to a string with + delimeter
word_with_spaces = ' '.join(sys.argv[2:])
word = '+'.join(sys.argv[2:])
diki_link = f"https://www.diki.pl/slownik-angielskiego?q={word}"
print(f"{word_with_spaces}")

def get_page_html_code(address):
    body = requests.get(address)
    return body.text

# get a transcription
transcription_html_code = get_page_html_code(f"https://wooordhunt.ru/word/{word_with_spaces}")
transcription = re.search("transcription\">\s(.{1,20}?)</span>", transcription_html_code)

if transcription != None:
    print(transcription[1])
else:
    transcription = ["", ""]
    print("no transcription")

html_code = get_page_html_code(diki_link)
parser = BeautifulSoup(html_code, "html.parser")
meta_description = parser.select("meta[name=\"description\"]")

if len(meta_description) == 0:
    print("there is no a meta tag with a description")
    exit(0)

meta_description = str(meta_description[0])
#print(type(meta_description))
trainslation_match = re.search("- (.*)\s-\s(.*)' name", meta_description)

if trainslation_match == None:
    print("there is no match")
    exit(0)

# convert from a string ti a list
trainslation = trainslation_match[2].split("; ")

i = 1
for meaning in trainslation:
    print(f"{i} {meaning}")
    i += 1

#echo = word_with_spaces + " " + transcription[1] + " - " +  trainslation[0]
#echo = echo.replace("\n", "")
#os.system("echo " + echo + " | xclip -selection c")

print()
print(diki_link)
print("done")
exit(0)


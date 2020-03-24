import requests # Make URL requests
import re
from bs4 import BeautifulSoup # Filter through fetched HTML-code

def line_empty(line):
    return len(line.strip()) < 1

# Search criteria
fromDate = "2020/2/1" # Year/Month/Day
toDate = "2020/2/29"  # Year/Month/Day
page = 1 			  # Page
URL = "https://politi.dk/doegnrapporter?fromDate={}&toDate={}&newsType=D%C3%B8gnrapporter&page={}&district=Nordsjaellands-Politi".format(fromDate,toDate,page)

# Find pages based on search criteria
frontPage = requests.get(URL)
soup = BeautifulSoup(frontPage.content, "html.parser")
ngCtrl = soup.find('section', {'ng-controller': 'newsListController'})
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(ngCtrl))

# Save page content
for url in urls:	
	subPage = requests.get(url)
	bs = BeautifulSoup(subPage.content, "html.parser")
	content = bs.find("div", {"class": "rich-text"}) # Filter/find div by class name. Returns entire tags
	#print(content.text.strip()) # Strips the text from the tags

	
	file = open("../page_content/tmpfile{}.txt".format("test"), "w", encoding="UTF-8")

	lines = content.text.strip().split('\n') # Seperate content section by newline
	for line in lines:
	    if not line_empty(line):
	        file.write(line+'\n')
	file.close()

# Extract relevant data from content



'''
# Get HTML as text
page = requests.get(URL)

# Create soup object, which makes it possible to filter the HTML 
soup = BeautifulSoup(page.content, "html.parser")

print(soup.title.text)
if soup.title.text == "Runtime":
	print("Runtime Error!!!\n") 


# Filter/find div by class name. Returns entire tags
content = soup.find("div", {"class": "rich-text"})

# Strips the text from the tags
#print(content.text.strip())


# Find the second p-tag with the certain class. This returns a date 
Dato = soup.findAll("p", {"class": "newsInfoText body-xmedium-police-regular dark-blue"})[1]
txt = Dato.text.strip()
#print(txt)


# Put content in txt-file
# Write to txt-file
file = open("tmpfile{}.txt".format(str(day1)+str(day2)), "w", encoding="UTF-8")

# Seperate content section by newline
lines = content.text.strip().split('\n')
for line in lines:
    if not line_empty(line):
        file.write(line+'\n')
file.close()
'''

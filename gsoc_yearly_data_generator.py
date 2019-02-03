import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen as uReq
import sys
import os
import warnings
import time
import random


warnings.filterwarnings("ignore")

def check(year):
	dataList = []
	with open("Data/ExtractedData.txt") as d:
            for l in d: dataList.append(l[0:len(l)-1])
	if year in dataList:
			print "This year data is already present, check " + "GSOC_"+str(year)+"_Data.ods"
			quit()

def extraction(year):
	num = random.randint(1,10000)
	check_file = "Data/ExtractedData.txt"
	file = open("Data/GSOC_"+str(year)+"_Data.ods", "w")
	
	with requests.Session() as c:
		page = c.get("https://summerofcode.withgoogle.com/archive/" + str(year) + "/organizations/")
		plain_text = page.text
		soup = BeautifulSoup(plain_text, "lxml")
		dict_year = {}
		gsoc_year_organizations = []
		for name in soup.findAll('h4',{'class': 'organization-card__name font-black-54'}):
			title = name.string
			gsoc_year_organizations.append(title)
			dict_year[title] = []

		i=0
		for link in soup.findAll('a',{'class': 'organization-card__link'}):
			hrefs = link.get('href')
			dict_year[gsoc_year_organizations[i]].append('https://summerofcode.withgoogle.com'+hrefs)
			i+=1

		count = i
		for i in gsoc_year_organizations:
			data = c.get(dict_year[i][0])
			data_text = data.text
			soup = BeautifulSoup(data_text, "lxml")
			for tag in soup.findAll('li',{'class': 'organization__tag--technology'}):
				tags = tag.string
				dict_year[i].append(tags.encode('utf-8'))
			file.write(i.encode('utf-8')+",")
			for k in range(len(dict_year[i])):
				if(k != len(dict_year[i])-1): file.write(dict_year[i][k]+",")
				else: file.write(dict_year[i][k]+"\n")
			print count
			count -=1

		file1 = open(check_file,"a+")
		file1.write(str(year)+"\n")
		file1.close()

if __name__ == "__main__":
	year = input("GSOC Year: ")
	extraction(year)

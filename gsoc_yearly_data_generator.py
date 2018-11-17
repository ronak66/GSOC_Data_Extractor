import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen as uReq
import sys
import os
import warnings
import time
import random


warnings.filterwarnings("ignore")

while(True):

	num = random.randint(1,10000)
	year = input("GSOC Year: ")
	file = open("GSOC_"+str(year)+"_Data.txt","w")
	check_file = "ExtractedData.txt"
	flag = 0
	file1 = open(check_file,"r")

	for line in file1:
		if(int(line) == year):
			print "This year data is already present, check " + "GSOC_"+str(year)+"_Data.txt"
			quit()
	file1.close()

	with requests.Session() as c:

		page = c.get("https://summerofcode.withgoogle.com/archive/" + str(year) + "/organizations/")
		plain_text = page.text
		soup = BeautifulSoup(plain_text, "lxml")
		dict_2018 = {}
		gsoc_2018_organizations = []
		for name in soup.findAll('h4',{'class': 'organization-card__name font-black-54'}):
			title = name.string
			gsoc_2018_organizations.append(title)
			dict_2018[title] = []


		i=0
		for link in soup.findAll('a',{'class': 'organization-card__link'}):
			hrefs = link.get('href')
			dict_2018[gsoc_2018_organizations[i]].append('https://summerofcode.withgoogle.com'+hrefs)
			i+=1

		# print i
		# for i in gsoc_2018_organizations:
		# 	print i+" " +dict_2018[i][0]
		count = i
		for i in gsoc_2018_organizations:
			data = c.get(dict_2018[i][0])
			data_text = data.text
			soup = BeautifulSoup(data_text, "lxml")
			for tag in soup.findAll('li',{'class': 'organization__tag--technology'}):
				tags = tag.string
				dict_2018[i].append(tags.encode('utf-8'))
			file.write(i.encode('utf-8')+",")
			for k in range(len(dict_2018[i])):
				if(k != len(dict_2018[i])-1): file.write(dict_2018[i][k]+",")
				else: file.write(dict_2018[i][k]+"\n")
			print count
			count -=1

		# print "---------------------------------"


		# for i in gsoc_2018_organizations:
		# 	for j in dict_2018[i]:
		# 		if(j == 'rails'): print i

		# page = c.get('https://summerofcode.withgoogle.com/archive/2017/organizations/')
		# plain_text = page.text
		# soup = BeautifulSoup(plain_text, "lxml")
		# gsoc_2017_organizations = []
		# for link in soup.findAll('h4',{'class': 'organization-card__name font-black-54'}):
		# 	title = link.string
		# 	gsoc_2017_organizations.append(title)
		# print "---------------------------------"
		#
		# common = []
		# for i in gsoc_2017_organizations:
		# 	if i in gsoc_2018_organizations:
		# 		common.append(i)
		#
		# for i in common: print i
		file1 = open(check_file,"a+")
		file1.write(str(year)+"\n")
		file1.close()
		break

import csv
from bs4 import BeautifulSoup
import requests

def printList(someList):
	for row in someList:
		print row

temp = []
starRate = []
revNum = []

with open('starRev.csv', 'rb') as r:
	starRevRead = csv.reader(r)
	for index, row in enumerate(starRevRead):
		if (index > 0):
			# print index, row[1]
			temp.append(row[1])
# printList(temp)

for index, i in enumerate(temp):
	if i == '#N/A':
		pass
		starRate.append('passed on ' + str(index + 2))
		revNum.append('passed on ' + str(index + 2))
		print 'N/A'
	else:
		print i
		r = requests.get(i)
		soup = BeautifulSoup(r.text, 'html.parser')
		stars = soup.find('meta', itemprop="ratingValue")
		starRating = stars["content"]
		reviews = soup.find(itemprop="reviewCount")
		reviewNum = reviews.text

		starRate.append(starRating)
		revNum.append(reviewNum)

rows = zip(temp, starRate, revNum)

with open('starRevWrite.csv', 'r+') as f:
    writer = csv.writer(f)
    for row in rows:
    	writer.writerow(row)

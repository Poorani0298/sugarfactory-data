from lxml import html
import cssselect 
import requests
import csv

#import glob

file = "./sugarfactory/List of Sugar Factories in tamil nadu State.html"
content = open(file).read()

tree = html.fromstring(content)    
company_names=tree.cssselect('div.search-item')
with open('lists.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["Company Name","Plant name","Address","Contact Details"])
	for company_name in company_names:
		writer.writerow([
		company_name.cssselect('h3')[0].cssselect('a')[0].text,
		company_name.cssselect('div div p')[0].cssselect('span')[0].text,
		company_name.cssselect('div div p')[1].cssselect('span')[0].text,
		company_name.cssselect('div div p')[2].cssselect('span')[0].text
		])

			
		

		# row=[company_name]
		# writer.writerow(row)



# with open('list.csv', 'w', newline='') as file:
	# 	writer = csv.writer(file)
	# 	writer.writerow(["SN", "Name", "detail"])
























			# print(company_name.cssselect('h3')[0].cssselect('a')[0].text)
			# writer.writerow(["SN", "Name", "Contribution"])
			# writer.writerow([1, "company_name.cssselect('div div p')[0].cssselect('span')[0].text"])
			# writer.writerow([2, "company_name.cssselect('div div p')[1].cssselect('span')[0].text"])
			# writer.writerow([3, "company_name.cssselect('div div p')[2].cssselect('span')[0].text"])
			# print("................................................................")



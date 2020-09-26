from lxml import html
import cssselect 
import requests
import csv
# files=["./sugarfactoryindia/Sugar Factories in India-1 - Anekant Prakashan.html","./sugarfactoryindia/Sugar Factories in India-2 - Anekant Prakashan.html","./sugarfactoryindia/Sugar Factories in India-3 - Anekant Prakashan.html","./sugarfactoryindia/Sugar Factories in India-4 - Anekant Prakashan.html","./sugarfactoryindia/Sugar Factories in India-5 - Anekant Prakashan.html"]
files=list(range(1,89))
with open('output.csv', 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(["Company Name","Plant name","Address","Contact Details"])
		for file_number in files:
			content = open("./sugarfactoryindia/Sugar Factories in India-{} - Anekant Prakashan.html".format(file_number)).read()
			tree = html.fromstring(content)    
			company_names=tree.cssselect('div.search-item')
			for company_name in company_names:
				writer.writerow([
				company_name.cssselect('h3')[0].cssselect('a')[0].text,
				company_name.cssselect('div div p')[0].cssselect('span')[0].text,
				company_name.cssselect('div div p')[1].cssselect('span')[0].text,
				company_name.cssselect('div div p')[2].cssselect('span')[0].text
				])


# urls=[
# 			'https://www.anekantprakashan.com/sugar-factories-in-ahmednagar/district',
#       'https://www.anekantprakashan.com/sugar-factories-in-akola/district',
#       'https://www.anekantprakashan.com/sugar-factories-in-aligarh/district',
#       'https://www.anekantprakashan.com/sugar-factories-in-ambala/district']
# for url in urls:
# 	page=requests.get(url)

# file = "./sugarfactory/www.anekantprakashan.com/sugar-factories/india"
# content = open(file).read()
# tree = html.fromstring(content)    
# company_names=tree.cssselect('div.search-item')
# with open('output.csv', 'w', newline='') as file:
# 	writer = csv.writer(file)
# 	writer.writerow(["Company Name","Plant name","Address","Contact Details"])
# 	for company_name in company_names:
# 		writer.writerow([
# 		company_name.cssselect('h3')[0].cssselect('a')[0].text,
# 		company_name.cssselect('div div p')[0].cssselect('span')[0].text,
# 		company_name.cssselect('div div p')[1].cssselect('span')[0].text,
# 		company_name.cssselect('div div p')[2].cssselect('span')[0].text
# 		])

			
		

		# row=[company_name]
		# writer.writerow(row)



# with open('list.csv', 'w', newline='') as file:
	# 	writer = csv.writer(file)
	# 	writer.writerow(["SN", "Name", "detail"])



# url([
# 	file.home/poorani/python_script/sugarfactory/
# 	www.anekantprakashan.com/sugar-factories-in-ahmednagar/
# 	district,
# 	file.home/poorani/python_script/sugarfactory/
# 	www.anekantprakashan.com/sugar-factories-in-akola/district,
# 	file.home/poorani/python_script/sugarfactory/
# 	www.anekantprakashan.com/sugar-factories-in-aligarh/district,
# 	file.home/poorani/python_script/sugarfactory/
# 	www.anekantprakashan.com/sugar-factories-in-ambala/district
# 		])





















			# print(company_name.cssselect('h3')[0].cssselect('a')[0].text)
			# writer.writerow(["SN", "Name", "Contribution"])
			# writer.writerow([1, "company_name.cssselect('div div p')[0].cssselect('span')[0].text"])
			# writer.writerow([2, "company_name.cssselect('div div p')[1].cssselect('span')[0].text"])
			# writer.writerow([3, "company_name.cssselect('div div p')[2].cssselect('span')[0].text"])
			# print("................................................................")



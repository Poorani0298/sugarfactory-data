from lxml import html
import cssselect
#import glob

file = "./sugarfactory/List of Sugar Factories in tamil nadu State.html"
content = open(file).read()

tree = html.fromstring(content)

company_names=tree.cssselect('div.search-item')
for company_name in company_names:
	print(company_name.cssselect('h3')[0].cssselect('a')[0].text)
	print(company_name.cssselect('div div p')[0].cssselect('span')[0].text)
	print(company_name.cssselect('div div p')[1].cssselect('span')[0].text)
	print(company_name.cssselect('div div p')[2].cssselect('span')[0].text)
	print("................................................................")


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

# company_details=tree.cssselect('div.search-item div div p')
# print(tree.cssselect('div.search-item div div p')[2].cssselect('span')[0].text)
# for company_detail in company_details:
# 	if len(company_detail.cssselect('span')) > 0:
# 		print(company_detail.cssselect('span')[0].text)


# print(tree.cssselect('b')[0].text)
# print(tree.cssselect('span.text'))
# print(tree.cssselect('b')[1].text)
# print(tree.cssselect('span.text'))
# print(tree.cssselect('b')[2].text)
# print(tree.cssselect('span.text'))
# print(tree.cssselect('div.search-item')[1].cssselect('h3.no-m')[1].cssselect('a')[1].text)
# # print(tree.cssselect('b')[3].text)




#book = tree.xpath('//span[@class="download-links"]/text()')
#span = tree.xpath('//span[@class="download-links"]')
# buyers = tree.xpath('//div[@title="buyer-name"]/text()')


#hrefs = tree.cssselect('span.download-links a')
#for href in hrefs:
#	print(href.attrib['href'])
# print(tree)
# print(tree.cssselect('ul.sub-menu li')[0].cssselect('a')[0].text)
# print(tree.cssselect('div.search-item')[0].cssselect('h3.no-m')[0].cssselect('a')[0].text)
# print(tree.cssselect('div.search-item div div p')[0].cssselect('span')[0].text)
# print(tree.cssselect('div.search-item div div p')[1].cssselect('span')[0].text)
# print(tree.cssselect('div.search-item div div p')[2].cssselect('span')[0].text)
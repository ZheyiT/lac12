import requests
from bs4 import BeautifulSoup

class CourseListing:
	def __init__(self, course_num, course_name):
		self.num = course_num
		self.name = course_name

	def __str__(self):
		return(self.num + ' ' + self.name + '\n\t' + self.description) 

	def init_from_details_url(self, details_url):
		global header #only inside this function
		page_text = requests.get(details_url, headers = header).text
		page_soup = BeautifulSoup(page_text, 'html.parser')
		self.description = page_soup.find(class_ = 'course2desc').text
		print(page_soup)


baseurl = 'https://www.si.umich.edu'
catalog_url = baseurl + '/programs/courses/catalog'
header = {'User-Agent': 'SI_CLASS'}
page_text = requests.get(catalog_url, headers=header).text
page_soup = BeautifulSoup(page_text, 'html.parser')


content_div = page_soup.find(class_='view-content')
#print(page_soup)

table_rows = content_div.find_all('tr')
course_listings = []
for i in range(4):
#for tr in table_rows:
	table_cells = tr.find_all('td')
	if len(table_cells) == 2:
		course_number = table_cells[0].text.strip()
		course_name = table_cells[1].text.strip()

		details_url_end = table_cells[0].find('a')['href']
		details_url = baseurl + details_url_end
		print(details_url)
		course_listing = CourseListing(course_number, course_name)
		course_listingc.init_from_details_url(details_url)
		course_listings.append(course_listing)

for cl in course_listings:
	print(cl)




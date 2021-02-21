import requests
from urllib.request import urlparse, urljoin
from urllib.parse import urlparse, urljoin
from requests_html import HTMLSession
from bs4 import BeautifulSoup

'''

-check if domain name at link contains company name or something similar




'''

visited = 0
redirects = []

def main():

	url1 = 'https://www.womenownedlogo.com/full-list'

	url2 = 'https://www.forbes.com/sites/kristenphilipkoski/2020/03/22/76-women-owned-small-businesses-to-support-from-a-distance/?sh=47aa56662241'

	url3 = 'https://www.forbes.com/sites/elisabethbrier/2020/06/05/100-black-owned-businesses-to-support/?sh=712a7c403660'

	crawl(url1, 0)

def isValid(site):

	parsed = urlparse(site)
	return bool(parsed.netloc) and bool(parsed.scheme)

def scrape(site):

	urls = set()
	domain = urlparse(site).netloc
	htmlsession = HTMLSession()
	response = htmlsession.get(site)
	try:
		response.html.render()
	except:
		pass

	s = BeautifulSoup(response.html.html,"html.parser")

	for a in s.findAll("a"):

		href = a.attrs.get("href")

		if href == "":
			continue

		if href is None:
			continue

		href = urljoin(site, href)
		parsed_href = urlparse(href)
		href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

		if not isValid(href):
			continue

		if domain not in href:
			if href not in urls:
				urls.add(href)
				print(href)

    #return urls

	#domain = site[site.find('.') + 1:site.rfind('.')]
	#print("Domain: " + domain)

	# getting the request from url 
	# r = requests.get(site)
    
    # converting the text

	# for link in s.find_all('a'):
	# 	print(s.find("a", href=True)["href"])

				# if site.index(domain) == -1:
				# 	print(href)


		#shouldn't contain part of website name between www. and .com, .net, etc.
				 #shouldn't be list of social media
				 #^^^put these into a text file and parse?

def crawl(url, count):

	max = 100

	allLinks = scrape(url)

	count += 1

	for link in allLinks:
		if link is None:
			continue
		if total > max:
			break
		crawl(link)



if __name__ == "__main__":
	main()

	'''

	make sure it comes after a category?
	make sure it does not include the sites own name
	make sure it is not squarespace or social media


	'''
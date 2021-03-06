from requests_html import HTMLSession
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import csv

external_urls = []

total_urls_visited = 0

def is_valid(url):

    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(url):
	domain_name = urlparse(url).netloc
	session = HTMLSession()
	response = session.get(url, verify=False)
	try:
	    response.html.render()
	except:
	    pass
	soup = BeautifulSoup(response.html.html, "html.parser")

	for a_tag in soup.findAll("a"):
	    href = a_tag.attrs.get("href")
	    if href == "" or href is None:
	        continue
	    href = urljoin(url, href)
	    parsed_href = urlparse(href)
	    href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
	    if not is_valid(href):
	        continue
	    if domain_name not in href:

	        href = str(href)
	        if href not in external_urls:
	            external_urls.append(href)
	            if ('instagram' in href) or ('facebook' in href) or ('cnn'  in href) or ('etsy'  in href) or ('linkedin'  in href) or ('twitter'  in href) or ('reddit'  in href) or ('pinterest'  in href) or ('zoom'  in href) or ('forbes'  in href) or ('tumblr'  in href) or ('deviantart'  in href) or ('imgur'  in href) or ('vimeo'  in href) or ('weheartit'  in href) or ('dailymotion'  in href) or ('youtube'  in href) or ('tiktok'  in href) or ('squarespace'  in href) or ('medium'  in href) or('foursquare'  in href) or ('triller'  in href) or ('techcrunch'  in href) or ('wordpress'  in href) or ('apple'  in href) or ('samsung'  in href):
	            	continue
	            else:
	                with open(f"{domain_name}_external_links.txt", "w") as f:
	                	print(href.strip(), file=f)
	                external_urls.append(href)

	        continue

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Link Extractor Tool with Python")
    parser.add_argument("url")
    
    args = parser.parse_args()
    url = args.url

    get_all_website_links(url)

    print("[+] Total External links:", len(external_urls))

    domain_name = urlparse(url).netloc

    with open(f"{domain_name}_external_links.txt", "w") as f:
        for href in external_urls:
            print(href.strip(), file=f)

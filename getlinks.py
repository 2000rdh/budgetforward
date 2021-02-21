from requests_html import HTMLSession
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import csv

# init the colorama module

# initialize the set of links (unique links)
external_urls = []

total_urls_visited = 0

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(url):
	"""
	Returns all URLs that is found on `url` in which it belongs to the same website
	"""
	# all URLs of `url`
	# domain name of the URL without the protocol
	domain_name = urlparse(url).netloc
	# initialize an HTTP session
	session = HTMLSession()
	# make HTTP request & retrieve response
	response = session.get(url, verify=False)
	# execute Javascript
	try:
	    response.html.render()
	except:
	    pass
	soup = BeautifulSoup(response.html.html, "html.parser")

	for a_tag in soup.findAll("a"):
	    href = a_tag.attrs.get("href")
	    if href == "" or href is None:
	        # href empty tag
	        continue
	    # join the URL if it's relative (not absolute link)
	    href = urljoin(url, href)
	    parsed_href = urlparse(href)
	    # remove URL GET parameters, URL fragments, etc.
	    href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
	    if not is_valid(href):
	        # not a valid URL
	        continue
	    if domain_name not in href:

	        href = str(href)
	        # external link
	        if href not in external_urls:
	            external_urls.append(href)


	            if ('instagram' in href) or ('facebook' in href) or ('cnn'  in href) or ('etsy'  in href) or ('linkedin'  in href) or ('twitter'  in href) or ('reddit'  in href) or ('pinterest'  in href) or ('zoom'  in href) or ('forbes'  in href) or ('tumblr'  in href) or ('deviantart'  in href) or ('imgur'  in href) or ('vimeo'  in href) or ('weheartit'  in href) or ('dailymotion'  in href) or ('youtube'  in href) or ('tiktok'  in href) or ('squarespace'  in href) or ('medium'  in href) or('foursquare'  in href) or ('triller'  in href) or ('techcrunch'  in href) or ('wordpress'  in href) or ('apple'  in href) or ('samsung'  in href):
	            	continue
	            else:
	                with open(f"{domain_name}_external_links.txt", "w") as f:
	                	print(href.strip(), file=f)
	                external_urls.append(href)

	        continue


# def crawl(url, max_urls=50):
#     """
#     Crawls a web page and extracts all links.
#     You'll find all links in `external_urls` and `internal_urls` global set variables.
#     params:
#         max_urls (int): number of max urls to crawl, default is 30.
#     """
#     global total_urls_visited
#     total_urls_visited += 1
#     links = get_all_website_links(url)
#     for link in links:
#         if total_urls_visited > max_urls:
#             break
#         crawl(link, max_urls=max_urls)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Link Extractor Tool with Python")
    parser.add_argument("url")
    
    args = parser.parse_args()
    url = args.url

    get_all_website_links(url)

    print("[+] Total External links:", len(external_urls))

    domain_name = urlparse(url).netloc


    # save the external links to a file
    with open(f"{domain_name}_external_links.txt", "w") as f:
        for href in external_urls:
            print(href.strip(), file=f)

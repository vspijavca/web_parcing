
# comments:
# css selector learning source: https://www.w3schools.com/cssref/css_selectors.asp
# soup objects use css selector sintax with method select - therefore if you would have read the documentation carefully you would have known that already

# problem 1 - resolved partialy. PLease finish it.
import requests
from bs4 import BeautifulSoup
import pprint

site = 'https://hub.packtpub.com/tag/python/' # the general link to the site

n = int(input('Enter the number of news inspected:'))


c = int(input('Enter value of comments you search:'))

def main(n=10, c=1):
	

	"This is the function that will get the n and c arguments and will call the needed code writen bellow"
	
	soup_object = iterate_pages(max_page=2)

	all_news = extract_news(soup_object)



	sorted_news = [ (x,y,z) for x, y, z in all_news if z  == c or z > c ] # check 3rd element(comment) from tupple if it satissfied us
	
	return sorted_news
	
def get_page_limit():
	"Get the maximum range of pages that must be iterated. Returns int value"

	res = requests.get(site)
	soup = BeautifulSoup(res.text, 'html.parser')

	pages = soup.select('div span[class=pages]') # get the element with the max page numbers
	text = pages[0].getText()

	last_character = text.split(' ')[-1] # isolate the max page number
	return last_character


def iterate_pages(max_page=2):
	"Iterate the entire range of news pages and return a list of soup objects. Each object representing the respective page content"

	page_list = list()

	res = requests.get(site)                     # parsing 1st page(it is unique link)
	soup = BeautifulSoup(res.text, 'html.parser')
	page_list.append(soup)

	for p in range(2, max_page+1, 1):            # parsing rest of web pages(repetitive links +1)
		page_link = site + "page/{}/".format(p)
		
		res = requests.get(page_link)
		soup = BeautifulSoup(res.text, 'html.parser')
		page_list.append(soup)

	return page_list # return list of strings


def extract_news(soup_object):
	"Function gets a soup object representing the entire page, then extracts only the news data out of it and packs them in a tuple "

	links = soup_object.select('div[class=td-block-span6] h3 a[rel=bookmark]')
	comments = soup_object.select('div[class=td-module-comments] a')
	
	news_attr = list()

	for n, comment in zip(links, comments):
		title = n.get('title')
		href = n.get('href')
		com = comment.getText()
		news_attr.append((title, href, com))

	return news_attr # return list of tuples


pprint(main())



# news_pages = iterate_pages(2)


# problem 2 - you must resolve it. Apply the same logic as in problem 1, but this time for site: https://feeder.co/discover/programming. Here you have a list of blog posts. Each blog post has a specific number of followers. You need to return a list of tuples. Each tuple has 3 mebers - title of the blog, link to the blog post, and number of followers. You must arange the tuples in the list in descending order according to the number of followers. 


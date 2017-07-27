
from general import *

class CrawlBot:

	user_url = ''
	links_crawled = set()

	def __init__(self, user_url):
		CrawlBot.user_url = user_url
		self.crawlpage(CrawlBot.user_url)

	@staticmethod
	def crawlpage(url):
		if url not in CrawlBot.links_crawled:
			print('Crawling ', url)
			CrawlBot.links_crawled.add(url)
			CrawlBot.get_links(url)
			

	@staticmethod
	def get_links(url):

		print(CrawlBot.links_crawled)

		parser = PageParser(url)

		return parser.parse_html()






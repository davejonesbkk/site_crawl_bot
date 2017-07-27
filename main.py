
from crawler import CrawlBot
#from general import *
import argparse

def get_data():
	parser = argparse.ArgumentParser()
	parser.add_argument('website_url', help='Enter the full url of your website')
	args = parser.parse_args()

	user_url = args.website_url

	start_crawl(user_url)


def start_crawl(user_url):

	print 'Starting ', user_url
	CrawlBot.crawlpage(user_url)



if __name__ == '__main__':
	get_data()
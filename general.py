

from bs4 import BeautifulSoup
import requests, argparse, pprint


class PageParser():

	def __init__(self, user_url):
		#super().__init__()
		self.user_url = user_url
		self.all_links = set()
		self.parsed_links = set()
		

	def parse_html(self):

		url = self.user_url

		r = requests.get(url)
		print 'Fetching ', url
		print 'Returns ', r.status_code

		self.all_links.add(url)

		soup = BeautifulSoup(r.text, 'html.parser')

		for s in soup.find_all('a'):
				print s.get('href')
				self.all_links.add(s.get('href'))



	def page_links(self):
		return self.all_links





		
				








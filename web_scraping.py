from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import time

def scrape_page(url):
  """This function do the scraping in one specific page,
  getting all the articles in it

  Args:
      url (string): Url of the site

  Raises:
      TypeError: In case of redirection, this causes a TypeError

  Returns:
      array: Returns all the articles obtained on the page
  """
  req = Request(
      url=url, 
      headers={'User-Agent': 'Mozilla/5.0'}
  )
  html = urlopen(req).read()
  soup = BeautifulSoup(html, 'html.parser')

  if hasattr(req, 'redirect_dict'):
    raise TypeError('Redirected to another page')

  cards = soup.find_all('article', {'class': 'post-h'})
  cards_info = []

  for card in cards:
    card_info = {}
    card_info['titulo'] = card.find('h2', {'class': 'post-h__content-title'}).getText()
    card_info['sub_titulo'] = card.find('p', {'class': 'post-h__content-sub'}).getText()

    card_info['tags'] = []
    tags = card.find('div', {'class': 'post-h__content-tags'}).find_all('span')
    for tag in tags:
      card_info['tags'].append(tag.get_text())

    card_info['link'] = card.find('div', {'class': 'post-h__content'}).find_all('a')[-1]['href']
    card_info['data'] = card.find('div', {'class': 'post-h__content-info'}).find_all('span')[0].getText()
    cards_info.append(card_info)
  return cards_info

def scrape_pages_interval(url, start, end):
  """This function scrapes a x number of pages, based on the interval
  passed

  Args:
      url (string): Base url used
      start (integer): Number of the first page
      end (integer): Number of the last page

  Returns:
      array: Return all the articles from all the pages joined
  """
  all_articles = []
  for page_number in range(start, end + 1):
      new_url = url + str(page_number)
      articles = scrape_page(new_url)
      all_articles = all_articles + articles
      time.sleep(1)
  return all_articles
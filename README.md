<h1 align="center"> Web Scraping API </h1>

![Python](https://img.shields.io/badge/python-v3.10-green) ![Flask](https://img.shields.io/badge/flask-v2.2-blue) ![BeautifulSoup](https://img.shields.io/badge/beautifulsoup-v4.11-blue) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)

This project is a web scraping api made to extract information from articles made by a brazilian technology site.

The endpoints available on this API are:
- <b>/last_articles</b>: this endpoint return all the articles on a interval of pages, based on these paramaters
    - start: page where the web scraping will start
    - end: last page where the web scraping will end
    - topic: brings all the articles based on a specific topic
    - tag: same as topic but based on the tags for the site
    > if no topic or tag is given, the last articles with no filter will be returned
- <b>/last_articles_topic</b>: this endpoint have the same functionality as the /last_article, but specific for topics
- <b>/last_articles_tag</b>: same as the /last_articles_topic but for tags

Beyond that, there's a dockerfile to build and run the application in a container.
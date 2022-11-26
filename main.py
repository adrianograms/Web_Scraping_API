from flask import Flask, request, jsonify
from web_scraping import scrape_pages_interval, scrape_page

app = Flask(__name__)
base_url = 'https://adrenaline.com.br/'

@app.route('/last_articles')
def last_articles():
    """Returns all the latestes articles from adrenaline. Can be filtred by
    topic or tag or none

    Returns:
        string: Returns all the articles in json format
    """
    try:
        start = int(request.args.get('start'))
        end = request.args.get('end')
        if end is None:
            end = start
        end = int(end)

        tag = request.args.get('tag')
        topic = request.args.get('topic')

        if not tag is None:
            url = base_url + 'noticias/assuntos/' + tag + '/pagina/'
        elif not topic is None:
            topic = topic.replace(' ','-')
            url = base_url + 'site/pesquisa/' + topic + '/pagina/'
        else:
            url = base_url + 'conteudos/ultimos/pagina/'
        
        articles = scrape_pages_interval(url, start, end)
        return jsonify(articles)
    except ValueError:
        return "Wrong type", 400
    except TypeError:
        return "Wrong paramaters", 400

@app.route('/last_articles_topic')
def last_articles_topic():
    """Returns all the latest articles based only on topics

    Returns:
        string: Return a json with all the articles
    """
    try:
        start = int(request.args.get('start'))
        end = request.args.get('end')
        if end is None:
            end = start
        end = int(end)
        topic = request.args.get('topic')

        url = base_url + 'site/pesquisa/' + topic + '/pagina/'
        articles = scrape_pages_interval(url, start, end)
        return jsonify(articles)
    except ValueError:
        return "Wrong type", 400
    except TypeError:
        return "Wrong paramaters", 400

@app.route('/last_articles_tag')
def last_articles_tag():
    """Returns all the latest articles based only on tags

    Returns:
        string: Return a json with all the articles
    """
    try:
        start = int(request.args.get('start'))
        end = request.args.get('end')
        if end is None:
            end = start
        end = int(end)
        tag = request.args.get('tag')

        url = base_url + 'noticias/assuntos/' + tag + '/pagina/'
        articles = scrape_pages_interval(url, start, end)
        return jsonify(articles)
    except ValueError:
        return "Wrong type", 400
    except TypeError:
        return "Wrong paramaters", 400

app.config['JSON_AS_ASCII'] = False
app.run(debug=True)
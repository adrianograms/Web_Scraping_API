FROM python:3.10

COPY requirements /usr/requirements

WORKDIR /usr

RUN pip install -r requirements
EXPOSE 5000

COPY web_scraping.py /usr/web_scraping.py
COPY app.py /usr/app.py


CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
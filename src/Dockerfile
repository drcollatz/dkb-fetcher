FROM python

WORKDIR /usr/src/dkb_fetcher
COPY requirements.txt .
#RUN apt-get update && apt-get install -y libxml2-dev libxslt1-dev zlib1g-dev python-dev gcc
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
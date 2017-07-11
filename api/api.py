"""This API methods file."""

from bottle import run, get, response

import requests
import re
import json


def count_words(url=None, word=None):
    link = "http://{0}".format(url)
    r = requests.get(link)
    # total words
    return len(re.findall(r"\b{text}\b".format(text=word), r.text))


@get('/count/<url>/<word>')
def api_search(url, word):
    response.content_type = 'application/json'
    status = 200
    total = 0
    try:
        total = count_words(url, word)
        msg = "ok"
    except Exception, e:
        print e
        status = 400
        msg = "error"
        pass

    response.status = status
    result = {"total": total, "url_details": [{"access": msg, "url": url}], "word": word}
    return json.dumps(result)

run(host='localhost', port=8000, debug=True)

"""This API methods file."""

import json
import sys
from bottle import run, get, response

sys.path.append("..")

from common.base import BaseCom


@get('/count/<url>/<word>')
def api_search(url, word):
    base = BaseCom()
    response.content_type = 'application/json'
    status = 200
    total = 0
    try:
        total = base.count_words(url, word)
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

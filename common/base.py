
import os
import requests
import re


class BaseCom(object):

    def __init__(self, *args, **kwargs):
        self.url_get = "http://localhost:8000/count/"
        self.base_dir = os.getcwd()

    def count_words(self, url=None, word=None, html_test=None):
        if html_test:
            html = html_test
        else:
            link = "http://{0}".format(url)
            r = requests.get(link)
            html = r.text
        # total words
        return len(re.findall(r"\b{text}\b".format(text=word), html, re.IGNORECASE))

    def get_html_text(self, name, type_file):
        path = "{0}/valueobject/{1}.{2}".format(self.base_dir, name, type_file)
        html = None
        try:
            with open(path, "r") as data:
                html = data.read()
        except Exception, e:
            print e
            pass

        return html

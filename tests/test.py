import requests

from common.base import BaseCom


class TestClass:

    base = BaseCom()
    URL_GET = base.url_get
    BASE_DIR = base.base_dir

    def test_get_200(self):
        """GET request to url returns a 200."""
        link = "www.python.org"
        word = "Python"
        url = '{0}{1}/{2}'.format(self.URL_GET, link, word)
        resp = requests.get(url)
        assert resp.status_code == 200

    def test_get_400(self):
        """GET request to url returns a 400."""
        link = "www.python.org22"
        word = "Python"
        url = '{0}{1}/{2}'.format(self.URL_GET, link, word)
        resp = requests.get(url)
        assert resp.status_code == 400

    def test_get_404(self):
        """GET request to url returns a 404."""
        url = '{0}'.format(self.URL_GET)
        resp = requests.get(url)
        assert resp.status_code == 404

    def test_count_globo(self):
        """Count word from text."""
        name = "globoesporte"
        type_file = "html"
        search = "cruzeiro"
        text_com = self.base.get_html_text(name, type_file)
        if text_com:
            total = self.base.count_words(html_test=text_com, word=search)
            assert total == 36
        else:
            assert 0

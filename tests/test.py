import requests

class TestClass:

    URL_GET = "http://localhost:8000/count/"

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

- [Python](https://www.python.org)
- [Botle](https://bottlepy.org/docs/dev/)
- [Requests](http://docs.python-requests.org/en/master/)


# Instalando a API:
* pip install -r requeriments.txt

# 1) Iniciando a aplicação:

```
$ cd api/
```
```
$ python api.py
```

# Exemplos
curl -i GET "http://localhost:8000/count/globoesporte.globo.com/Cruzeiro"
 ```json
 {"url_details": [{"access": "ok", "url": "globoesporte.globo.com"}], "total": 7, "word": "Cruzeiro"}
 ```

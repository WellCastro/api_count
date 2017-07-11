# Regra:

A Api considera a palavra em todo o conteúdo da URL informada, sendo assim a busca não é apenas por texto visível na navegação por um navegador, mas sim em todo o código da página.

## Exemplo: Palavra pesquisada => ave
 ``` html
 <h1>Avestruz<h1><p>ave</p>
 <img src="ave.jpg"></img>
  ```
 
 Resultado = 2 palavras encontradas(ave e ave.jpg)
 
# Tecnologia

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

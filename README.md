# Regra:

A Api considera a palavra em todo o conteúdo da URL informada, sendo assim a busca não é apenas por texto renderizado por um navegador, mas sim em todo o código da página.

## Exemplo: Palavra pesquisada => ave
 ``` html
 <h1>Avestruz<h1><p>Ave</p>
 <img src="ave.jpg" alt="ave"></img>
  ```
 
 Resultado = 2 palavras encontradas(Ave e ave)
 
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
 {"url_details": [{"access": "ok", "url": "globoesporte.globo.com"}], "total": 16, "word": "Cruzeiro"}
 ```


# Executando os testes:
Os testes criados são testes "smoke tests",  garatem que API está com o serviço básico executando.
Em uma nova aba do console, execute os seguintes comandos.
(Necessário a API rodando).

```
$ cd /tests
```
```
$ pytest test.py
```

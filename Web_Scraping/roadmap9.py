'''
MEU primeiro Web Scaper

clicar com o botão direito do mouse em um elemento da página e selecionar Inspecionar para abrir as ferramentas de desenvolvimento do navegador. 
Isso permite ver o código HTML da página e identificar as tags e classes que contêm as informações que desejamos.

from bs4 import BeautifulSoup
import urllib.request
mysite = urllib.request.urlopen('https://books.toscrape.com/').read()
soup_mysite = BeautifulSoup(mysite, 'html.parser')

div = soup_mysite.find(class_ = "article.product_pod")
p = div.find(class_ = "price_color")
print(div, "\n")
print( "=" * 50, "\n", p)
 
'''
from bs4 import BeautifulSoup
import urllib.request

mysite = urllib.request.urlopen('https://books.toscrape.com/').read()
# Ajuste do parser aqui:
soup_mysite = BeautifulSoup(mysite, 'html.parser')

# 1. Encontra o contentor pai do primeiro livro
livro = soup_mysite.find(class_="product_pod")

# 2. Extrai o preço (o que você já fez perfeitamente!)
preco = livro.find(class_="price_color").text

# 3. Extrai o link e o título (eles estão dentro da tag <h3> <a>)
tag_link = livro.find('h3').find('a')
titulo = tag_link['title'] # O BeautifulSoup vai buscar o atributo 'title'
link_final = tag_link['href']

print(f"Livro Encontrado:")
print(f"Título: {titulo}")
print(f"Preço:  {preco}")
print(f"Link:   {link_final}")
print("\n" + "=" * 50 + "\n" + "=" * 50 + "\n")

'''
1. Comandos de Localização (Onde está o campo?)
Estes comandos servem para identificar a "caixa" onde a informação vive.

soup.find('tag'): Encontra a primeira ocorrência de uma tag (ex: soup.find('h3')).
soup.find_all('tag'): Encontra todas as ocorrências (ex: soup.find_all('tr') para linhas de uma tabela).
soup.select('seletor_css'): Permite usar seletores de CSS, que são muito mais poderosos para campos complexos (ex: soup.select('div.product_pod > h3 > a')).

2. Comandos de Extração de Conteúdo (O que está escrito lá?)
Depois de localizar o campo, você precisa de extrair o que está lá dentro:

elemento.text: Extrai apenas o texto visível para o utilizador (ex: o preço "£51.77").
elemento.get('atributo') ou elemento['atributo']: Extrai o valor de um atributo técnico (o "tipo" de dados escondido).
Exemplo: Para o exercício das notícias, para extrair o link, você usa elemento['href'].

3. Comandos de Identificação de Classe e ID
Para diferenciar um cabeçalho (th) de uma linha de dados (td), usamos estas propriedades:

elemento.name: Devolve o nome da tag (ex: retorna "tr" ou "th").
elemento.get('class'): Devolve a lista de classes CSS daquele campo.
Dica: Se o elemento.get('class') for igual a ['header'], você sabe que é um cabeçalho. Se for ['data-row'], sabe que é um dado.

Objetivo | Comando Recomendado
Aceder a um valor (link, src) | elemento['nome_do_atributo']
Aceder ao texto (preço, título) | elemento.text.strip()
Saber que tag é (tr, td, h1) | elemento.name
Saber a classe CSS (para filtrar) | elemento.get('class')
'''
print("Tabela - Wikipédia")

url_wiki = 'https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o'
disfarce = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

pedido = urllib.request.Request(url_wiki, headers=disfarce)

mysite_table = urllib.request.urlopen(pedido).read()
soup_mysite_table = BeautifulSoup(mysite_table, 'html.parser')

tabela = soup_mysite_table.select_one("table.wikitable.sortable")

if tabela:
    linhas = tabela.select('tr')[1:] #Saltar o th cabeçalho

    for linha in linhas:
        coluna_pais = linha.select_one("td a")

        if coluna_pais:
            nome_pais = coluna_pais.text.strip()
            link_pais = coluna_pais['href']
            
            print(f"País: {nome_pais} | Link: https://pt.wikipedia.org{link_pais}")
else:
    print("Tabela não encontrada! Verifique o seletor CSS.")


print("\n" + "=" * 50 + "\n" + "=" * 50 + "\n")
print("Tabela - Hacker")

url_hackersite = 'https://news.ycombinator.com/'
disfarce_hacker = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

pedido_hacker = urllib.request.Request(url_hackersite, headers=disfarce_hacker)

mysite_hacker = urllib.request.urlopen(pedido_hacker).read()
soup_mysite_hacker = BeautifulSoup(mysite_hacker, 'html.parser')

tabela_hacker = soup_mysite_hacker.select_one("#hnmain")
if tabela_hacker:
    linhas = tabela_hacker.select('tr.athing')

    for linha in linhas:
        coluna_link = linha.select_one (".titleline > a")

        if coluna_link:
            titulo_hacker = coluna_link.text
            link_hacker = coluna_link['href']
            print(f"Link: {titulo_hacker}")
            print(f"URL:  {link_hacker}")
            print("-" * 50)

else:
    print("Tabela não encontrada! Verifique o seletor CSS.")
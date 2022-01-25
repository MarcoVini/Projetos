# ferramenta de coleta de dados web, permite a extração de dados da web convertendo em informações estruturadas para
# análise. Utilizado para Pentester.

from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br').content
#recebendo conteúdo do site html.
soup = BeautifulSoup(site, 'html.parser')
#baixando o html do site
# print(soup.prettify())
#transforma html em string e exibe na tela.

temperatura = soup.find('span', class_="-bold -gray-dark-2 -uppercase -font-12 _padding-5")

print(soup.a.string)
print(soup.title.string)
print(temperatura.string)
print(soup.find('admin'))
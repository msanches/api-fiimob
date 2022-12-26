import requests
from bs4 import BeautifulSoup

def scraping():
    data = []
    headers = {"User-Agent":"Mozilla/5.0"}
    #Busca pelo código html da página que será analisada
    res = requests.get('https://www.fundsexplorer.com.br/ranking', headers=headers)
    soup = BeautifulSoup(res.content, 'lxml')#html.parser
    rows = soup.find('table', {'id': 'table-ranking'}).find('tbody').find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        temp = {'fundo': cols[0].text,
                'setor': cols[1].text,
                'valorAtual': cols[2].text.replace('R$', '').replace('.','').replace(',','.').strip(),
                'liquidezDiaria':cols[3].text,
                'provento': cols[4].text.replace('R$', '').replace('.','').replace(',','.').strip(),
                'dividendoYieldAno': cols[12].text.replace('%','').replace(',','.').strip(),
                'variacaoPreco': cols[13].text.replace('%', '').replace('.','').replace(',','.').strip(),
                'patrimonioLiquido': cols[16].text.replace('R$', '').replace('.','').replace(',','.').strip(),
                'vpa': cols[17].text.replace('R$', '').replace('.','').replace(',','.').strip(),
                'pvpa': cols[18].text.replace(',','.').strip(),
                'qteAtivos': cols[25].text
                }
        data.append(temp)
    return data

def fundo(nomeFundo):
    nomeFundo = nomeFundo.upper() + '11'
    data = scraping()
    for ele in data:
        if ele['fundo'] == nomeFundo:
            return(ele)

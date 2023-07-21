from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd

# creating a webdriver instance
driver = webdriver.Chrome('TEBD\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)


def get_alimentos(soup):
  # pegando todos os alimentos da pagina
  result_all = []
  for alimento in soup.find_all('tr'):
    caracteristicas = alimento.find_all('a')
    result = [th for th in caracteristicas]
    result_all.append(result)

  # infos iniciais dos alimentos
  df = pd.DataFrame()
  base = 'http://www.tbca.net.br/base-dados/'
  for i in range (len(result_all)):
    if i==0: continue
    row_data = {}
    row_data['url'] = base + result_all[i][0]['href']
    row_data['codigo'] = result_all[i][0].text
    row_data['nome'] = result_all[i][1].text
    row_data['nome_ingles'] = result_all[i][2].text
    row_data['nome_cientifico'] = result_all[i][3].text
    row_data['grupo'] = result_all[i][4].text
    row_data['marca'] = result_all[i][5].text

    row_df = pd.DataFrame.from_records([row_data])
    df = pd.concat([df, row_df], ignore_index=True)

  return df


def composicao_alimento(soup, cod_alimento):
  soup = soup.find('table', class_='display dataTable no-footer')

  result_all = []
  for item in soup.find_all('tr'):
    caracteristicas = item.find_all('td')
    result = [th for th in caracteristicas]
    result_all.append(result)

  # composicao dos alimentos
  df = pd.DataFrame()
  df.loc[0, 'codigo'] = cod_alimento
  for i in range (len(result_all)):
    if i==0: continue
    df.loc[0, result_all[i][0].text + f' ({result_all[i][1].text})'] = result_all[i][2].text
  
  return df


# trocando as paginas
alimentos = pd.DataFrame()
for page in range(1, 58):
  driver.get(f"http://www.tbca.net.br/base-dados/composicao_alimentos.php?pagina={page}&atuald=1")
  soup = bs(driver.page_source, 'lxml') # parseamento

  alimentos_page = get_alimentos(soup)
  alimentos = pd.concat([alimentos, alimentos_page], ignore_index=True)

# composicao dos alimentos
df_final = pd.DataFrame()
temp = pd.DataFrame()
for index, row in alimentos.iterrows():
  driver.get(row['url'])
  
  soup = bs(driver.page_source, 'lxml') # parseamento
  comp_item = composicao_alimento(soup, row['codigo'])
  temp = alimentos.merge(comp_item, on='codigo')
  df_final = pd.concat([df_final, temp], ignore_index=True)

# salvando o arquivo da coleta
df_final.to_csv('data/csv/tbca.csv', encoding='utf-8', index=False)
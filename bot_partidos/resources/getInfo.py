from bs4 import BeautifulSoup
import requests
import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

def get_info(url):
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'html.parser')

    header = soup.div.h2
    nombre_liga, categoria, fase, grupo, vuelta = str(header).split('<br/>', 4)

    jornada_box = soup.find("div", attrs={'id':'jornada_numero'})
    numero_jornada, date = str(jornada_box).split('<br/>', 4)

    data = []
    tabla_box = soup.find('div', attrs={'class':'resultados'})

    rows = tabla_box.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    del data[0]
    dataSQV = []
    for element in data:
        if len(element) > 3:
            if 'SANT QUIRZE' in str(element[0]) or 'SANT QUIRZE' in str(element[1]):
                dataSQV.append(element)



    msg = ""

    msg += remove_tags(nombre_liga) + '\n'
    msg += remove_tags(grupo) + '\n'
    msg += remove_tags(numero_jornada) + '\n \n'

    for element in dataSQV:
        msg += 'Local: '+ element[0] + '\n'
        msg += 'Visitant: '+ element[1] + '\n'
        msg += 'Día: '+ element[2] + '\n'
        msg += 'Hora: '+ element[3] + '\n'
        msg += 'Lloc: '+ element[4] + '\n \n'

    return msg

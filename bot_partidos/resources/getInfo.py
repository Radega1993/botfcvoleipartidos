from bs4 import BeautifulSoup
import requests
import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

def get_info():
    req = requests.get('http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4092')
    #equipo = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4092'

    #soup = BeautifulSoup(pageHtml, "xml")
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

    for element in data:
        if len(element) > 3:
            if 'SANT QUIRZE' in str(element[0]) or 'SANT QUIRZE' in str(element[1]):
                local = element[0]
                visitante = element[1]
                dia = element[2]
                hora = element[3]
                lugar = element[4]


    msg = ""

    msg += remove_tags(nombre_liga) + '\n'
    msg += remove_tags(grupo) + '\n'
    msg += remove_tags(numero_jornada) + '\n \n'

    msg += 'Local: '+ remove_tags(local) + '\n'
    msg += 'Visitant: '+ remove_tags(visitante) + '\n'
    msg += 'Día: '+ remove_tags(dia) + '\n'
    msg += 'Hora: '+ remove_tags(hora) + '\n'
    msg += 'Lloc: '+ remove_tags(lugar) + '\n'

    return msg

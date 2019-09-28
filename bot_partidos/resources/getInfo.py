from bs4 import BeautifulSoup
import requests


def get_info():
    req = requests.get('http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4092')
    #equipo = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4092'

    #soup = BeautifulSoup(pageHtml, "xml")
    soup = BeautifulSoup(req.text, 'html.parser')

    header = soup.div.h2
    nombre_liga, categoria, fase, grupo, vuelta = str(header).split('<br/>', 4)

    print(nombre_liga)
    print(categoria)
    print(grupo)
    print(vuelta)

    jornada_box = soup.find("div", attrs={'id':'jornada_numero'})
    numero_jornada, date = str(jornada_box).split('<br/>', 4)
    print(numero_jornada)
    print(date)

    tabla_box = soup.find('div', attrs={'class':'resultados'})

    tabla = tabla_box.text.strip()
    msg = ""
    '''
    msg += name + '\n'

    msg += jornada + '\n'
    '''

    lista = tabla.split("  ")[8:]

    for element in lista:
        msg += element + '\n'

    print(msg)

    '''
    name_box = soup.find('div', attrs={'id':'nombre_competicion'})
    jornada_box = soup.find('div', attrs={'id':'jornada_numero'})
    tabla_box = soup.find('div', attrs={'class':'resultados'})

    name = name_box.text.strip()
    jornada = jornada_box.text.strip()
    tabla = tabla_box.text.strip()

    msg = ""
    msg += name + '\n'

    msg += jornada + '\n'


    lista = tabla.split("  ")[8:]

    for element in lista:
        msg += element + '\n'
    '''

    return "msg"

get_info()

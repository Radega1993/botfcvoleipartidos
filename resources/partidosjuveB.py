from bs4 import BeautifulSoup
import urllib2

def jornadaJuveB():
	quote_page = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=2433'

	page = urllib2.urlopen(quote_page)
	pageHtml = page.read()
	page.close()
	soup = BeautifulSoup(pageHtml, "lxml")




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

	return msg
from resources.getInfo import get_info


def get_url(equipo):

    if equipo == 'infn':
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4050'
        return get_info(url)
    elif equipo == 'infv':
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4120'
        return get_info(url)
    elif equipo == 'infb':
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4120'
        return get_info(url)
    elif equipo == 'infr':
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4114'
        return get_info(url)
    elif equipo == 'cadn':
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4040'
        return get_info(url)
    elif equipo == 'cadv':
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4094'
        return get_info(url)
    elif equipo == 'cadb':
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4092'
        return get_info(url)
    elif equipo == 'juvn':
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4038'
        return get_info(url)
    elif equipo == 'juvv':
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4093'
        return get_info(url)
    elif equipo == 'jubb':
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4091'
        return get_info(url)
    else:
        url = 'http://competicio.fcvoleibol.cat/competiciones.asp?v=18&torneo=4031'
        return get_info(url)

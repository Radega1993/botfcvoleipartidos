def get_url(equipo):

    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return equipo

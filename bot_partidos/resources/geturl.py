def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

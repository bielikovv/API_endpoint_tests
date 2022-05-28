import requests

def get_info(tag):
    sym = '$!?/.,><|}{)(";:*^%#@~`'
    if '#' in tag:
        tag = tag.replace('#', '')
        for el in tag:
            if el in sym:
                raise SyntaxError('Тэг не может содержать специальные символы')
        if len(tag) != 9:
            raise AssertionError('Некорректный тэг')
    else:
        raise AssertionError('Некорректный тэг')
    if tag != tag.upper():
        raise ValueError('Тэг должен быть в верхнем регистре!')
    HEADERS = {'Authorization': 'Bearer CLASH_ROYALE_API_TOKEN'}
    url = 'https://api.clashroyale.com/v1/players/%23{}/'
    data = requests.get(url.format(tag), headers=HEADERS).json()
    if data == {'reason': 'notFound'}:
        raise FileExistsError('Данные не существуют')
    return data

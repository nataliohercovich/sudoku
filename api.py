import requests


def api(tam):
    resp = requests.get(
        'http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=' +
        '&size=' +
        str(tam)
        )

    lista = [[0 for j in range(tam)] for i in range(tam)]

    for item in resp.json()["squares"]:
        lista[item["y"]][item["x"]] = str(item["value"])

    return lista
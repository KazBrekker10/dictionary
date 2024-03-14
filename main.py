import json
def search (keyword):
  with open ('index.json', "r") as file:
    words = json.load(file)
    for word in words:
      if keyword in word['keywords']:
        return word
      else:
        print('no se encontro el termino en le indice')


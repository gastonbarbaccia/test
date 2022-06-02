import requests, json, csv, os
from datetime import datetime
from enviar_email import email
import zipfile
import shutil
import pathlib

dt = datetime.now()
fecha_hora = (dt.strftime('%d%m%Y_%H%M%S'))

#Sonarqube
#URL = "https://sonarqube.gscorp.ad/api/issues/search"
#TOKEN = "e336512579a791fc83f8bf7fbe1c007be084e166"

#Sonarqubede
URL = "https://sonarqubede.gscorp.ad/api/issues/search"
TOKEN = "b4c0e98ae1ba95fa97c284391302daca685f2eb8"


projects_list = {}

ubicacion_absoluta = "C:\\Users\\004257613\\Downloads\\SonarScript"

def Consulta():
    #cantidad de registros por página. Máximo: 500
    ps = 500
    DATA = {'p':1,'ps':ps}
    requests.packages.urllib3.disable_warnings()
    r = requests.get(url = URL, params = DATA, headers={"Accept": "*/*"}, auth=(TOKEN, ''), verify=False)
    response = r.json()
    # cantidad registros
    q = response["total"]
    pages = 1
    output = []

    while (q > 0):
        pages+=1
        #saco el page size a la cantidad de registros. 
        q -= ps
    #creo un objeto iterable, con un rango entre uno y la cantidad de páginas previamente obtenida.
    pages = range(1,pages)
    for page in pages:
        DATA = {'p':page,'ps':ps}
        r = requests.get(url = URL, params = DATA, headers={"Accept": "*/*"}, auth=(TOKEN, ''), verify=False)
        response = r.json()
        issues = ''
        issues = response.get('issues')
        for issue in issues:
            o = {}
            o["key"]=issue["key"]
            o["project"]=issue["project"]
            o["creationDate"]=issue["creationDate"]
            o["updateDate"]=issue["updateDate"]
            output.append(o)
    return output


if __name__ == '__main__':
    Consulta()